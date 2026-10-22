from django.test import SimpleTestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class PublicPageTests(SimpleTestCase):
	page_names = ('home', 'about', 'services', 'contact')

	def test_all_public_pages_render_the_shared_shell_and_booking_button(self):
		for page_name in self.page_names:
			with self.subTest(page=page_name):
				response = self.client.get(reverse(f'clinic:{page_name}'))

				self.assertEqual(response.status_code, 200)
				self.assertContains(response, '<main id="main-content"', html=False)
				self.assertContains(response, 'Book Appointment')
				self.assertContains(response, 'static/clinic/css/site.css')
				self.assertContains(response, 'static/clinic/js/appointment.js')
				self.assertContains(response, '+91 99459 88815')
				self.assertContains(response, '+91 080 2653 4899')

	def test_confirmed_navigation_routes_exist(self):
		for page_name in self.page_names:
			with self.subTest(page=page_name):
				self.assertEqual(self.client.get(reverse(f'clinic:{page_name}')).status_code, 200)

	def test_home_has_approved_highlights_and_services_link(self):
		response = self.client.get(reverse('clinic:home'))

		for phrase in (
			'Advanced Heart Care',
			'You Can Trust.',
			'Senior Specialist',
			'Interventional Expertise',
			'Evening Consultations',
			'Our Services',
			'landing_page_hero.jpeg',
		):
			with self.subTest(phrase=phrase):
				self.assertContains(response, phrase)

	def test_about_contains_profile_qualifications_experience_and_academic_figures(self):
		response = self.client.get(reverse('clinic:about'))

		for phrase in (
			'about_page.jpeg',
			'Education &amp; Qualifications',
			'Karnataka Medical College, Hubli',
			'MR Medical College, Gulbarga',
			'IMS BHU, Varanasi',
			'University Hospitals, Cleveland Medical Center, USA',
			'Awarded 3 Fellowships in Cardiology',
			'30+ years of clinical and academic experience',
			'JSS Medical College, Mysore',
			'JN Medical College, Belgaum',
			'NIMS, Hyderabad',
			'G.B. Pant Hospital, New Delhi',
			"St. John's Medical College, Bangalore",
			'Belhoul Apollo, Dubai',
			'Narayana Health, Bangalore',
			'Currently Performing',
			'Coronary Angiography',
			'Angioplasty (PTCA)',
			'Also Performed Throughout Career',
			'Pacemaker Implantation',
			'Mitral Valvuloplasty (PTMC)',
			'Device Closure of ASD &amp; PDA',
			'Peripheral Angioplasty',
			'Tumour Embolisation',
			'Publications',
			'Years of Clinical Research',
			'Conference Presentations',
			'International Conferences Attended',
			'Abstracts &amp; Indexed Journals',
			'Thesis Works',
		):
			with self.subTest(phrase=phrase):
				self.assertContains(response, phrase)

		for figure in ('16', '15+', '10', '22', '30', '3'):
			self.assertContains(response, f'>{figure}<', html=False)

	def test_services_show_only_approved_descriptions_without_detail_actions(self):
		response = self.client.get(reverse('clinic:services'))

		for phrase in ('Consultation', 'Blood Test', 'ECG', 'personalised care plan'):
			with self.subTest(phrase=phrase):
				self.assertContains(response, phrase)
		self.assertNotContains(response, 'Learn more')
		self.assertNotContains(response, 'service-detail')

	def test_contact_has_approved_address_hours_and_named_map(self):
		response = self.client.get(reverse('clinic:contact'))

		for phrase in (
			'Heart Care Centre',
			'1202, 35th B Cross, 28th Main',
			'Jayanagar 4th T Block',
			'Bangalore',
			'560041',
			'Monday',
			'6:00 PM',
			'8:30 PM',
			'title="Heart Care Centre Location"',
		):
			with self.subTest(phrase=phrase):
				self.assertContains(response, phrase, html=False)

	def test_online_booking_patient_forms_and_appointment_route_are_absent(self):
		for page_name in self.page_names:
			response = self.client.get(reverse(f'clinic:{page_name}'))
			self.assertNotContains(response, 'Book your appointment online')
			self.assertNotContains(response, 'href="/appointment"', html=False)
			self.assertNotContains(response, '<form', html=False)

		self.assertEqual(self.client.get('/appointment/').status_code, 404)
		with self.assertRaises(NoReverseMatch):
			reverse('clinic:appointment')