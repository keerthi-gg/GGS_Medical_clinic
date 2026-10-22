# Quickstart and Validation: GGS Medical Clinic Public Website

## Repository Status

The Django project, clinic app, dependency manifests, Tailwind CLI scripts, and smoke/acceptance
tests are now present. The commands below have been verified in the project environment on
Windows 11 with Python 3.13.6, Node 24.14.0, and npm 11.9.0. The pinned Python baseline is 3.12+
and the npm audit reported no known vulnerabilities at setup time.

## Prerequisites to Confirm During Setup

- Python 3.12 or newer is required for Django 6.1.
- Node.js and npm are required for the Tailwind CLI build.
- Install Python dependencies from `requirements-dev.txt`, npm packages using `npm ci`, and the
   Chromium browser binary using Playwright's installer.
- No application secrets are expected for this public site. Do not add credentials or real values
  to example environment files. Confirm whether any non-secret environment configuration is needed.

## Local Setup Commands

```powershell
python --version
node --version
npm --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
npm ci
python -m playwright install chromium
```

If PowerShell blocks virtual-environment activation, use the approved local Python environment
activation method; do not change machine-wide execution policy as an undocumented workaround.

## Run and Test Commands

```powershell
npm run css:build
python manage.py check
python manage.py test
python -m pytest
python manage.py runserver
```

At the time of final implementation validation, `python -m pytest` passed 18 tests: seven Django
page/scope tests and eleven Playwright browser tests. Browser checks passed at 320 CSS px without
horizontal overflow, validated keyboard navigation and modal focus containment, and exercised
copy success/failure plus blocked media and normal static asset delivery. A manual browser review
sampled text/background contrast; the checked pairs exceeded 4.5:1. Re-run after changes; these
results describe the tested revision.

Keyboard interaction, responsive reflow, focus containment, and sampled text/background contrast
were manually reviewed in the browser. A full assistive-technology review with a physical screen
reader remains pending; this work is not a formal WCAG conformance certification. Complete that
review on supported devices before final clinic acceptance, and do not claim compliance based only
on the automated checks or sampled contrast results.

`python manage.py check --deploy` is a production-settings review, not a local run command. Run
it with `DJANGO_DEBUG=false`, a private `DJANGO_SECRET_KEY`, and the intended
`DJANGO_ALLOWED_HOSTS`. The current check reports HSTS, HTTPS redirect, and secure CSRF cookie
warnings because no production host or TLS-termination setup has been selected. Resolve these with
the chosen host/proxy configuration before deployment; do not silence them or enable HSTS blindly.
Django's development server is not a production server. Serve generated static assets using the
selected production host's supported approach; Django documents `collectstatic` as part of
static-file deployment.

## Validation Scenarios

1. **Django page responses**: Verify Home, About, Services, and Contact resolve directly and return
   successful responses; assert navigation targets and required copy, both phone numbers, and
   correct image static paths.
2. **Scope regression**: Assert no `/appointment` booking route, booking form, patient entry,
   staff UI, service-detail route, or Services “Learn more” control is rendered.
3. **Appointment popup**: In Playwright, open the shared header dialog from each page; verify its
   title, both phone numbers, copy icon labels, Escape and close-button behavior, focus containment,
   and focus return to the opener.
4. **Copy outcomes**: Stub clipboard success and denied/unavailable cases. Confirm appropriate
   success/failure feedback and that numbers remain visible and selectable in both cases.
5. **Broken assets and map**: Intercept/abort portrait requests and the Google Maps embed; confirm
   doctor identification, address, hours, and both numbers remain available.
6. **Responsive and accessibility review**: Test 320 CSS px, a wider mobile viewport, and desktop.
   Manually verify keyboard navigation, visible focus, zoom/reflow, labels, contrast, and applicable
   WCAG 2.2 AA criteria. Automated tests do not certify WCAG conformance.
7. **Documentation and privacy review**: From a clean environment, follow the final setup/run/test
   instructions. Confirm no secret values are committed and no patient data flow or storage exists.