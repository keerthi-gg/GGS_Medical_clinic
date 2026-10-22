import re

from playwright.sync_api import expect


def test_home_shell_and_static_stylesheet(page, clinic_server):
    page.goto(clinic_server)

    expect(page).to_have_title(re.compile(r'GGS Medical Clinic$'))
    expect(page.locator('main#main-content')).to_have_count(1)

    stylesheet_url = page.locator('link[rel="stylesheet"]').get_attribute('href')
    assert stylesheet_url is not None
    assert 'static/clinic/css/site.css' in stylesheet_url

    stylesheet_response = page.request.get(f'{clinic_server}{stylesheet_url}')
    assert stylesheet_response.status == 200


def test_static_script_and_both_portrait_assets_are_served(page, clinic_server):
    page.goto(clinic_server)

    script_url = page.locator('script[src*="appointment.js"]').get_attribute('src')
    assert script_url is not None
    assert page.request.get(f'{clinic_server}{script_url}').status == 200
    expect(page.locator('.hero-image')).to_have_attribute('src', re.compile(r'landing_page_hero\.jpeg$'))
    expect(page.locator('.hero-image')).to_have_js_property('complete', True)
    assert page.locator('.hero-image').evaluate('(image) => image.naturalWidth > 0')

    page.goto(f'{clinic_server}/about/')
    expect(page.locator('.about-image')).to_have_attribute('src', re.compile(r'about_page\.jpeg$'))
    expect(page.locator('.about-image')).to_have_js_property('complete', True)
    assert page.locator('.about-image').evaluate('(image) => image.naturalWidth > 0')


def test_navigation_and_appointment_dialog_on_every_page(page, clinic_server):
    routes = ('/', '/about/', '/services/', '/contact/')

    for route in routes:
        page.goto(f'{clinic_server}{route}')
        expect(page.get_by_role('navigation', name='Main navigation')).to_be_visible()
        expect(page.get_by_role('button', name='Book Appointment').first).to_be_visible()
        page.get_by_role('button', name='Book Appointment').first.click()

        dialog = page.get_by_role('dialog', name='Book an appointment by phone')
        expect(dialog).to_be_visible()
        expect(dialog.get_by_role('link', name='+91 99459 88815')).to_be_visible()
        expect(dialog.get_by_role('link', name='+91 080 2653 4899')).to_be_visible()
        expect(dialog.get_by_text('Call reception to arrange your consultation. The website does not take bookings.')).to_be_visible()
        expect(dialog.get_by_role('button', name='Copy mobile reception number')).to_be_visible()
        expect(dialog.get_by_role('button', name='Copy landline reception number')).to_be_visible()
        page.keyboard.press('Escape')
        expect(dialog).not_to_be_visible()
        expect(page.get_by_role('button', name='Book Appointment').first).to_be_focused()


def test_appointment_dialog_close_button_and_copy_success(page, clinic_server):
    page.goto(clinic_server)
    page.evaluate("""() => {
      Object.defineProperty(navigator, 'clipboard', {
        configurable: true,
        value: { writeText: async (value) => { window.__copiedPhone = value; } }
      });
    }""")

    trigger = page.get_by_role('button', name='Book Appointment').first
    trigger.click()
    dialog = page.get_by_role('dialog', name='Book an appointment by phone')
    dialog.get_by_role('button', name='Copy mobile reception number').click()
    expect(dialog.get_by_text('Copied +91 99459 88815')).to_be_visible()
    assert page.evaluate('window.__copiedPhone') == '+91 99459 88815'
    dialog.get_by_role('button', name='Close appointment information').click()
    expect(dialog).not_to_be_visible()
    expect(trigger).to_be_focused()


def test_appointment_dialog_keyboard_open_and_focus_containment(page, clinic_server):
    page.goto(clinic_server)
    trigger = page.get_by_role('button', name='Book Appointment').first
    trigger.focus()
    page.keyboard.press('Enter')

    dialog = page.get_by_role('dialog', name='Book an appointment by phone')
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role('button', name='Close appointment information')).to_be_focused()

    for _ in range(12):
        page.keyboard.press('Tab')
        expect(dialog).to_contain_text('Book an appointment by phone')
        assert page.evaluate('document.activeElement.closest("dialog") !== null')


def test_copy_failure_selects_phone_number(page, clinic_server):
    page.goto(clinic_server)
    page.evaluate("""() => {
      Object.defineProperty(navigator, 'clipboard', {
        configurable: true,
        value: { writeText: async () => { throw new DOMException('Denied', 'NotAllowedError'); } }
      });
    }""")

    page.get_by_role('button', name='Book Appointment').first.click()
    dialog = page.get_by_role('dialog', name='Book an appointment by phone')
    dialog.get_by_role('button', name='Copy landline reception number').click()
    expect(dialog.get_by_text('Copy unavailable. +91 080 2653 4899 is selected; copy it manually.')).to_be_visible()
    expect(dialog.get_by_role('link', name='+91 080 2653 4899')).to_be_visible()
    assert page.evaluate('window.getSelection().toString()') == '+91 080 2653 4899'


def test_all_page_links_resolve_and_services_has_no_learn_more(page, clinic_server):
    page.goto(clinic_server)
    navigation = page.get_by_role('navigation', name='Main navigation')

    for label, path in (
        ('Home', '/'),
        ('About the doctor', '/about/'),
        ('Services', '/services/'),
        ('Contact', '/contact/'),
    ):
        link = navigation.get_by_role('link', name=label)
        expect(link).to_be_visible()
        response = page.request.get(f'{clinic_server}{path}')
        assert response.status == 200

    page.goto(f'{clinic_server}/services/')
    expect(page.get_by_role('heading', name='Consultation')).to_be_visible()
    expect(page.get_by_role('heading', name='Blood Test')).to_be_visible()
    expect(page.get_by_role('heading', name='ECG')).to_be_visible()
    expect(page.get_by_text('Learn more')).to_have_count(0)
    expect(page.locator('.service-item a')).to_have_count(0)


def test_keyboard_navigation_activates_each_page_link(page, clinic_server):
    page.goto(clinic_server)
    page.get_by_role('link', name='About the doctor').focus()
    page.keyboard.press('Enter')
    expect(page).to_have_url(f'{clinic_server}/about/')
    expect(page.get_by_role('heading', name='About Dr. G.G. Shetty')).to_be_visible()

    page.get_by_role('link', name='Services').focus()
    page.keyboard.press('Enter')
    expect(page).to_have_url(f'{clinic_server}/services/')
    expect(page.get_by_role('heading', name='Our Services')).to_be_visible()

    page.get_by_role('link', name='Contact').focus()
    page.keyboard.press('Enter')
    expect(page).to_have_url(f'{clinic_server}/contact/')
    expect(page.get_by_role('heading', name='Contact & Location')).to_be_visible()


def test_broken_portraits_keep_doctor_identified(page, clinic_server):
    page.route('**/static/clinic/images/**', lambda route: route.abort())

    page.goto(clinic_server)
    expect(page.locator('.hero-image')).to_have_attribute('src', re.compile(r'landing_page_hero\.jpeg$'))
    expect(page.get_by_role('heading', name='Advanced Heart Care You Can Trust.')).to_be_visible()
    expect(page.get_by_text('Dr. G.G. Shetty', exact=True).first).to_be_visible()
    expect(page.locator('.hero-image')).to_be_hidden()
    expect(page.locator('.hero-image-wrap .image-fallback')).to_be_visible()

    page.goto(f'{clinic_server}/about/')
    expect(page.locator('.about-image')).to_have_attribute('src', re.compile(r'about_page\.jpeg$'))
    expect(page.get_by_role('heading', name='About Dr. G.G. Shetty')).to_be_visible()
    expect(page.locator('.about-image')).to_be_hidden()
    expect(page.locator('.about-image-wrap .image-fallback')).to_be_visible()


def test_blocked_map_does_not_hide_contact_information(page, clinic_server):
    page.route('https://www.google.com/maps/**', lambda route: route.abort())
    page.goto(f'{clinic_server}/contact/')

    expect(page.get_by_text('Heart Care Centre', exact=True)).to_be_visible()
    expect(page.get_by_text('1202, 35th B Cross, 28th Main')).to_be_visible()
    expect(page.get_by_text('Jayanagar 4th T Block')).to_be_visible()
    expect(page.locator('.contact-details').get_by_role('link', name='+91 99459 88815')).to_be_visible()
    expect(page.locator('.contact-details').get_by_role('link', name='+91 080 2653 4899')).to_be_visible()
    expect(page.get_by_text('6:00 PM – 8:30 PM')).to_be_visible()


def test_mobile_layout_has_no_page_wide_horizontal_overflow(page, clinic_server):
    page.set_viewport_size({'width': 320, 'height': 900})

    for route in ('/', '/about/', '/services/', '/contact/'):
        page.goto(f'{clinic_server}{route}')
        overflow = page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
        assert not overflow, f'Horizontal overflow found at {route}'