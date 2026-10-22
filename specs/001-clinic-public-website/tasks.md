---

description: "Dependency-ordered implementation tasks for the GGS Medical Clinic public website"
---

# Tasks: GGS Medical Clinic Public Website

**Input**: Design documents from `specs/001-clinic-public-website/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, and `quickstart.md`

**Tests**: Automated regression tests are required by FR-016. Use Django's test runner for route,
template, and content checks and pytest/Playwright for browser interactions. Add tests in each story
phase before that story's implementation tasks; no test-first/red-green requirement is imposed.

**Organization**: Tasks are grouped by independently testable user story in priority order.

## Format: `[ID] [P?] [Story] Description`

- **[P]** means the task edits files independent of other unfinished tasks in the same phase.
- **[Story]** identifies the specification user story; setup, foundational, and polish tasks omit it.
- Every task names its target path. Paths below follow the proposed structure in `plan.md` and are
  not claims that those application files already exist.

## Scope Boundaries

Do not add online booking, patient-data collection/storage, patient accounts, staff dashboard,
appointment management, clinic domain models/database persistence, analytics, tracking, service
detail pages, replacement “Learn more” actions, or unapproved integrations. The Google Maps embed
is the only agreed external integration. React remains reference-only. No application API contract
is needed. Do not select or add a production host or deployment infrastructure in these tasks.

## Phase 1: Setup

**Purpose**: Create reproducible dependency manifests before relying on setup or test commands.

- [X] T001 [P] Add pinned Django runtime dependencies and the selected Python baseline to `requirements.txt`.
- [X] T002 [P] Add pytest, pytest-django, and Playwright test dependencies to `requirements-dev.txt`.
- [X] T003 [P] Add Tailwind CSS CLI build scripts and compatible pinned development dependencies to `package.json` and generate `package-lock.json`.
- [X] T004 Create the Django project entry point and `config/settings.py`, `config/urls.py`, `config/asgi.py`, and `config/wsgi.py` per `plan.md`; do not create clinic domain models or patient storage.
- [X] T005 Create the `clinic` app package and its route/view/test directories in `clinic/urls.py`, `clinic/views.py`, and `clinic/tests/test_pages.py`.

## Phase 2: Foundational Work

**Purpose**: Establish shared rendering, navigation structure, static assets, and browser-test configuration required by all stories.

- [X] T006 Configure Django template discovery and app-namespaced static-file handling in `config/settings.py`.
- [X] T007 Connect the clinic URL configuration to the project URL configuration in `config/urls.py` and `clinic/urls.py`.
- [X] T008 Add the shared document shell, navigation slots, page title blocks, and static CSS/JavaScript references to `clinic/templates/clinic/base.html`.
- [X] T009 Add Tailwind input CSS and the project-local generated CSS output paths to `clinic/static/clinic/css/input.css` and `clinic/static/clinic/css/site.css`; ensure the CLI scans `clinic/templates/clinic/` through `package.json`.
- [X] T010 Configure pytest and Playwright browser-test discovery without adding website runtime dependencies in `pytest.ini` and `requirements-dev.txt`.
- [X] T011 Add a static-asset and route smoke-test foundation in `clinic/tests/test_pages.py` and `tests/e2e/test_public_site.py`.

## Phase 3: User Story 1 - Find Telephone Appointment Information (Priority: P1)

**Goal**: Visitors can open the same appointment dialog from every page, read both numbers, and copy either number without entering patient data.

**Independent Test**: On each page, open the shared dialog; verify both phone numbers and telephone-only wording, copy success and failure behavior, manual selection fallback, keyboard dismissal, and focus return.

### Tests for User Story 1

- [X] T012 [US1] Add Playwright tests for the shared appointment button, both numbers, dialog labeling, Escape/close behavior, and focus return in `tests/e2e/test_public_site.py`.
- [X] T013 [US1] Add Playwright tests for clipboard success, denied/unavailable failure feedback, and selectable phone numbers in `tests/e2e/test_public_site.py`.
- [X] T014 [US1] Add Django regression assertions that all page responses contain the shared booking entry point and no online-booking route or patient-entry form in `clinic/tests/test_pages.py`.

### Implementation for User Story 1

- [X] T015 [US1] Add the persistent “Book Appointment” header button and labeled native modal dialog with both confirmed numbers to `clinic/templates/clinic/base.html`.
- [X] T016 [US1] Add accessible close control, initial focus, Escape dismissal, focus containment, and focus return behavior for the dialog in `clinic/static/clinic/js/appointment.js`.
- [X] T017 [US1] Add a labeled copy icon beside each number, success/failure announcements, and manual-selection fallback in `clinic/templates/clinic/base.html` and `clinic/static/clinic/js/appointment.js`.
- [X] T018 [US1] Replace online-booking claims in Home-facing appointment copy with telephone-only instructions in `clinic/templates/clinic/home.html`.

## Phase 4: User Story 2 - Find Clinic Location and Hours (Priority: P1)

**Goal**: Visitors can find the written clinic address, reception numbers, consultation hours, and map; contact details remain usable if the map fails.

**Independent Test**: Open Contact directly, verify the full address, both numbers, hours, and named map; block the map and verify all written contact details remain available.

### Tests for User Story 2

- [X] T019 [US2] Add Django tests for Contact route, full address, both phone numbers, consultation hours, and accessible map title in `clinic/tests/test_pages.py`.
- [X] T020 [US2] Add a Playwright test that blocks or aborts the map request and verifies address, hours, and phone numbers remain visible in `tests/e2e/test_public_site.py`.

### Implementation for User Story 2

- [X] T021 [US2] Render the confirmed address, reception numbers, and Monday-Friday consultation hours in `clinic/templates/clinic/contact.html`.
- [X] T022 [US2] Add the supplied Google Maps embed with a descriptive title and lazy loading to `clinic/templates/clinic/contact.html`; keep written contact information independent of the embed.

## Phase 5: User Story 5 - Navigate on Mobile, Desktop, and Keyboard (Priority: P1)

**Goal**: Visitors can reach all four pages and use the shared controls on keyboard, mobile, and desktop layouts.

**Independent Test**: Open each route directly and traverse shared navigation with keyboard at mobile and desktop sizes; verify visible focus, current-page indication, no overlap/clipping, and no horizontal page overflow at 320 CSS pixels.

### Tests for User Story 5

- [X] T023 [US5] Add Django route and navigation-target assertions for Home, About, Services, and Contact in `clinic/tests/test_pages.py`.
- [X] T024 [US5] Add Playwright navigation, keyboard-focus, and 320-pixel reflow checks in `tests/e2e/test_public_site.py`.

### Implementation for User Story 5

- [X] T025 [US5] Add keyboard-operable links for Home, About the doctor, Services, and Contact with a current-page indication in `clinic/templates/clinic/base.html`.
- [X] T026 [US5] Add responsive Tailwind layout and visible focus styles for shared navigation, booking button, and dialog controls in `clinic/templates/clinic/base.html` and `clinic/static/clinic/css/input.css`.
- [X] T027 [US5] Add the Home “Our Services” link to the Services route in `clinic/templates/clinic/home.html`.

## Phase 6: User Story 3 - Understand the Doctor's Background (Priority: P2)

**Goal**: Visitors can review the approved Home introduction/highlights and complete About profile with the correct portraits.

**Independent Test**: Compare Home and About independently against `oldui.txt`; verify all required sections and figures, correct portrait placement, and doctor identification when either image request fails.

### Tests for User Story 3

- [X] T028 [US3] Add Django assertions for Home introduction, all three highlights, About qualifications, experience, specializations, and six academic/research figures in `clinic/tests/test_pages.py`.
- [X] T029 [US3] Add Playwright checks for Home/About portrait paths and doctor identification after portrait requests fail in `tests/e2e/test_public_site.py`.

### Implementation for User Story 3

- [X] T030 [US3] Add the Home hero, approved introduction, three highlights, and telephone-only appointment wording in `clinic/templates/clinic/home.html`.
- [X] T031 [US3] Add the About profile, affiliations, qualifications, experience, current-versus-career specializations, and academic/research figures in `clinic/templates/clinic/about.html`.
- [X] T032 [US3] Copy `landing_page_hero.jpeg` and `about_page.jpeg` into `clinic/static/clinic/images/landing_page_hero.jpeg` and `clinic/static/clinic/images/about_page.jpeg`, then reference them on Home and About respectively.
- [X] T033 [US3] Add descriptive image alternative text and layout behavior that preserves doctor identification when either portrait is unavailable in `clinic/templates/clinic/home.html` and `clinic/templates/clinic/about.html`.

## Phase 7: User Story 4 - Review Clinic Services (Priority: P2)

**Goal**: Visitors can read exactly the three approved service descriptions without unsupported controls or additional service-detail pages.

**Independent Test**: Open Services directly and verify Consultation, Blood Test, and ECG descriptions appear, while no “Learn more” control or service-detail link is present visually or in keyboard navigation.

### Tests for User Story 4

- [X] T034 [US4] Add Django assertions for the three approved service titles/descriptions and absence of “Learn more” text or detail links in `clinic/tests/test_pages.py`.
- [X] T035 [US4] Add a Playwright keyboard/DOM regression check that Services exposes no replacement service action or service-detail link in `tests/e2e/test_public_site.py`.

### Implementation for User Story 4

- [X] T036 [US4] Render only Consultation, Blood Test, and ECG with their supplied descriptions in `clinic/templates/clinic/services.html`; do not add buttons, links, or detail routes.

## Phase 8: Polish and Cross-Cutting Concerns

**Purpose**: Complete project documentation, privacy/scope review, and accessibility/responsive acceptance checks.

- [X] T037 [P] Document confirmed prerequisites, environment variables with safe placeholders, and exact verified setup/run/test commands in `README.md` and `specs/001-clinic-public-website/quickstart.md`.
- [X] T038 Add a regression check that rejects unapproved `/appointment` routes, online-booking language, patient-entry controls, and service-detail actions in `clinic/tests/test_pages.py`.
- [X] T039 [P] Review dependencies and Django settings for unused admin/authentication/database features and confirm no patient data, accounts, analytics, tracking, or unapproved integration was added in `requirements.txt`, `requirements-dev.txt`, `package.json`, and `config/settings.py`.
- [X] T040 Run the documented Django, Playwright, and Tailwind checks after their project scripts exist; update `specs/001-clinic-public-website/quickstart.md` with commands that were actually verified.
- [ ] T041 Complete a full manual review of all pages and the appointment dialog at 320 CSS pixels, wider mobile, and desktop sizes, including assistive-technology checks against applicable WCAG 2.2 AA criteria; record final results in `specs/001-clinic-public-website/quickstart.md`. Browser keyboard, responsive, and sampled contrast checks have been performed, but the screen-reader review is still pending.
- [X] T042 Verify generated Tailwind CSS contains classes used by Django templates and that static paths resolve in development in `package.json`, `clinic/static/clinic/css/site.css`, and `clinic/tests/test_pages.py`.

## Dependencies and Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Establish manifests and Django project/app structure; no story work starts before these exist.
- **Foundational (Phase 2)**: Configure routes, templates, static assets, and test discovery; blocks all user stories.
- **User Stories (Phases 3-7)**: Begin after Foundation. P1 stories are US1, US2, and US5; P2 stories are US3 and US4. US2, US3, and US4 are independently verifiable once Foundation is ready. US1 requires the shared base template. US5 completes shared navigation; its layout checks should be repeated after story pages land.
- **Polish (Phase 8)**: Depends on all desired story work; final accessibility and documentation checks gate acceptance.

### User Story Dependencies

- **US1 (P1)**: Depends on foundational `base.html` and static JavaScript/CSS paths; independently test the dialog and copy behavior on all four rendered route shells.
- **US2 (P1)**: Depends on foundation and its Contact template/route; independent of other story content.
- **US5 (P1)**: Depends on foundation; test direct routes and shared navigation. Re-run responsive checks after US3/US4 content is integrated.
- **US3 (P2)**: Depends on Home/About routes and static asset configuration; independent of US2 and US4.
- **US4 (P2)**: Depends on the Services route; independent of other page content.

### Parallel Opportunities

- Setup dependency-manifest tasks T001 and T002 can proceed in parallel; T003 may proceed in parallel with them because it edits only the npm manifest and lockfile. Django project generation T004 follows dependency decisions; T005 follows project setup.
- After Foundation, US2 Contact, US3 profile pages, and US4 Services can be developed independently, provided each task stays within its listed files. US1 dialog work and US5 shared-header navigation both modify `base.html`; do not execute those edits in parallel.
- In each story, tests and implementation tasks target some of the same test/template files and are ordered; do not mark them parallel.
- Polish documentation (T037) and the independent static dependency/scope review (T039) can proceed in parallel after the implementation files exist. Final verification tasks follow their prerequisites.

## Implementation Strategy

### MVP First

1. Complete Setup and Foundational phases.
2. Complete US1 so visitors can access both appointment numbers from the shared header.
3. Complete US2 so written contact details are available even when the map is unavailable.
4. Validate these P1 journeys independently before expanding the site content.

### Incremental Delivery

1. Add US5 shared navigation and verify all four routes.
2. Add US3 Home and About content and correctly mapped portraits.
3. Add US4 service descriptions with no unsupported actions.
4. Complete final accessibility, privacy/scope, test, and setup-documentation checks.

Do not treat the MVP sequence as permission to ship incomplete WCAG, privacy, or constitution requirements. All applicable gates remain required before acceptance.