# Implementation Plan: GGS Medical Clinic Public Website

**Branch**: `001-clinic-public-website` | **Date**: 2026-10-21 | **Spec**: [spec.md](spec.md)

**Input**: [Feature specification](spec.md) and `.specify/memory/constitution.md`

## Summary

Create one server-rendered Django informational site with four pages and one shared header.
Preserve the approved React reference content and layout intent in Django Templates. Compile
Tailwind CSS to a Django static asset. Use a native modal dialog for the shared “Book Appointment”
control; show the two confirmed phone numbers with copy icons, accessible feedback, and manual-copy
fallback. No appointment, patient, or staff data is submitted or stored. Validation uses Django
request/template tests plus browser-level Playwright checks for interactions, responsive layout,
and media failure. This plan defines structure and validation only; it does not implement them.

## Technical Context

**Language/Version**: Python 3.12 minimum (Django 6.1 documentation supports Python 3.12+).
Confirm the available interpreter before environment setup.

**Primary Dependencies**: Django 6.1; Tailwind CSS CLI 4.x through npm as a build-time tool;
pytest and Playwright's Python pytest plugin for browser acceptance tests. Pin compatible versions
and commit lock/dependency files during project setup. Tailwind and Playwright are not runtime
website dependencies.

**Storage**: No application data store or domain models. Static clinic content and contact details
are rendered by the site; no patient information is collected or persisted.

**Testing**: Django's built-in test runner for route/template/content regression; pytest with
Playwright for real-browser navigation, popup, clipboard, broken-image, blocked-map, and responsive
checks. Manual keyboard and WCAG 2.2 AA review remains required.

**Target Platform**: Current evergreen desktop and mobile browsers; Django development server for
local validation. A production host and static-asset serving configuration are not selected here.
Clipboard writing requires a secure context in browsers; validate production behavior over HTTPS.

**Project Type**: Single Django web application; server-rendered pages, static CSS/images, and
small browser-side behavior for the appointment dialog and clipboard controls.

**Performance Goals**: No numeric target is specified. Keep pages and contact information usable
without waiting for the third-party map; load the map lazily as in the reference.

**Constraints**: Exactly four agreed pages; phone-only appointments; no online patient data,
booking, staff workflow, database-backed feature, account, analytics, tracking, or unapproved
integration. Google Maps embed is the only agreed external integration. Target WCAG 2.2 AA.

**Scale/Scope**: Four public pages, shared navigation/header, one appointment dialog, three service
descriptions, two supplied portraits, one external map embed. No authenticated users or business
data lifecycle.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Research Gate: PASS

- **Workflow and evidence**: The clarified spec names all pages and user journeys; the old UI is
  treated as reference evidence, with explicit phone-booking and service-button overrides.
- **Privacy and security**: No patient data, accounts, forms, staff tools, or patient storage are
  planned. Do not add analytics or expose details through logs/errors.
- **Architecture and scope**: Django/Python, Django Templates, and Tailwind CSS are confirmed.
  One Django project is proposed; React is not included as a runtime.
- **Accessibility and responsive behavior**: WCAG 2.2 AA is the target; native dialog behavior,
  keyboard operation, focus return, copy feedback, and mobile/desktop checks are included.
- **Testing and maintainability**: Add focused automated route/content/browser regressions and
  manual keyboard/accessibility review; keep changes to the four-page website.
- **Documentation and secrets**: Quickstart records verified commands and labels commands that
  cannot be run until the not-yet-created application scaffold exists. Examples use placeholders.

### Post-Design Gate: PASS

The proposed structure contains no patient entities, APIs, database feature, staff subsystem,
extra service actions, or unapproved external services. The map remains an external dependency;
its failure cannot hide the written address, hours, or phone numbers. The chosen dialog and static
asset pipeline support rather than replace the required accessibility and failure testing.

## Project Structure

### Documentation (this feature)

```text
specs/001-clinic-public-website/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── spec.md
├── checklists/requirements.md
└── tasks.md                 # Created later by /speckit-tasks
```

No `contracts/` directory is planned: this site exposes no application API or data contract.
The supplied Google Maps iframe is an embed consumed by the browser, not a new clinic API.

### Source Code (repository root; proposed for implementation)

```text
manage.py
config/
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py
clinic/
├── urls.py
├── views.py
├── templates/clinic/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── services.html
│   └── contact.html
├── static/clinic/
│   ├── css/input.css
│   ├── css/site.css          # Generated Tailwind output
│   ├── js/appointment.js
│   └── images/
│       ├── landing_page_hero.jpeg
│       └── about_page.jpeg
└── tests/
    └── test_pages.py         # Django route/template/content regression
tests/
└── e2e/
    └── test_public_site.py   # pytest-playwright browser acceptance tests
package.json                  # Tailwind CLI build scripts (development only)
package-lock.json
requirements.txt              # Runtime Python dependencies
requirements-dev.txt          # Browser/test tooling
```

**Structure Decision**: One Django project package (`config`) and one public-site app
(`clinic`) keep routes, shared templates, static assets, and focused tests together. A separate
frontend project is unnecessary because rendering is server-side. The exact project package and
dependency files will be created during implementation; the tree above is a proposed target, not
an assertion that these files currently exist.

## Complexity Tracking

No constitution violations or extra application subsystems are proposed. Django plus a CSS build
tool and browser test runner are the minimum planning choices needed to meet the confirmed stack
and validation requirements.
