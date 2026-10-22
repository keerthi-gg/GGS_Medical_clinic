# Feature Specification: GGS Medical Clinic Public Website

**Feature Branch**: Not created; feature directory is independent of branch naming.
**Created**: 2026-10-20
**Status**: Clarified - ready for planning
**Input**: Build the initial informational clinic website from the supplied UI reference,
with telephone-only appointments, four agreed pages, and no online patient-data collection.

## Clarifications

### Session 2026-10-21

- Q: How should visitors access the clinic's appointment phone numbers from the website? → A: Show a "Book Appointment" button in the shared top banner on every page. Activating it opens a popup with both phone numbers and a copy icon beside each number.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Find Telephone Appointment Information (Priority: P1)

As a visitor, I want to find both reception numbers and understand how to arrange a consultation
without entering personal information online.

**Why this priority**: Calling reception is the only agreed appointment workflow.
**Independent Test**: Open Contact directly and find both numbers and consultation hours without
visiting another page or submitting information. On each page, open the appointment popup and
copy either number.

**Acceptance Scenarios**:

1. **Given** Contact is open, **When** a visitor reads Reception & Booking, **Then** both
   +91 99459 88815 and +91 080 2653 4899 are visible with an instruction to call for appointments.
2. **Given** any appointment-related wording, **When** a visitor reads it, **Then** it describes
   telephone booking, never online booking, availability, or an appointment confirmed by the site.
3. **Given** any of the four pages is open, **When** the visitor activates "Book Appointment"
  in the shared top banner, **Then** a popup displays both numbers and the instruction to call,
  without requesting patient information.
4. **Given** the popup is open, **When** the visitor activates the copy control beside either
  number, **Then** that number is copied and the visitor receives clear success feedback.
5. **Given** clipboard access is unavailable or denied, **When** the visitor activates a copy
  control, **Then** the number remains visible and selectable and the visitor receives a clear
  message that copying did not succeed.
6. **Given** the visitor calls reception, **When** the receptionist handles the appointment,
   **Then** the website does not request, receive, or store the patient's details.

### User Story 2 - Find Clinic Location and Hours (Priority: P1)

As a visitor, I want the clinic address and hours so I can plan a visit.

**Why this priority**: Visitors need practical information even when an external map is unavailable.
**Independent Test**: Open Contact directly, read the complete address and hours, and repeat with
the map blocked.

**Acceptance Scenarios**:

1. **Given** Contact is open, **When** its information is read, **Then** it shows Heart Care Centre,
   1202, 35th B Cross, 28th Main, Jayanagar 4th T Block, Bangalore - 560041, and consultation hours
   Monday-Friday, 6:00 PM-8:30 PM.
2. **Given** the map is available, **When** Contact loads, **Then** the supplied map embed appears
   with an accessible name describing the clinic location.
3. **Given** the map is blocked, slow, or unavailable, **When** Contact is used, **Then** the written
   address, hours, and both phone numbers remain readable and usable without waiting for the map.

### User Story 3 - Understand the Doctor's Background (Priority: P2)

As a visitor, I want the doctor's introduction and professional background to understand the
supplied information about the clinician.

**Why this priority**: The supplied profile explains who provides care and their experience.
**Independent Test**: Review Home and About independently against their respective reference sections.

**Acceptance Scenarios**:

1. **Given** Home is opened directly, **When** the page is read, **Then** the supplied introduction,
   three highlights (Senior Specialist, Interventional Expertise, Evening Consultations), and
   Home portrait appear, with telephone wording replacing the old online-booking claim.
2. **Given** About is opened directly, **When** the visitor reads it, **Then** the profile,
   qualifications, experience, specializations, and academic/research information from the
   reference appear with the About portrait.
3. **Given** specialization content, **When** it is read, **Then** currently performed procedures
   remain distinct from those performed throughout the career; neither list becomes an invented
   list of services offered at this clinic.
4. **Given** either portrait fails, **When** the page is read, **Then** the doctor remains identified
   by text and descriptive alternative text, with no developer file instructions exposed.

### User Story 4 - Review Clinic Services (Priority: P2)

As a visitor, I want to read the three supplied clinic service descriptions without encountering
controls that promise unavailable information.

**Why this priority**: Visitors need a clear, bounded description of the clinic's services.
**Independent Test**: Open Services directly and compare the three descriptions with the reference.

**Acceptance Scenarios**:

1. **Given** Services is open, **When** the visitor reviews it, **Then** Consultation, Blood Test,
   and ECG appear with their supplied descriptions and without invented additional services.
2. **Given** any service listing, **When** it is inspected visually and with keyboard navigation,
   **Then** there are no "Learn more" controls, replacement actions, or service-detail links.

### User Story 5 - Navigate on Mobile, Desktop, and Keyboard (Priority: P1)

As a visitor, I want to move between the four pages and read their content regardless of screen
size or whether I use a keyboard.

**Why this priority**: All visitor journeys depend on usable navigation and readable content.
**Independent Test**: Traverse all four navigation destinations using only the keyboard on mobile
and desktop layouts; open each destination directly as well.

**Acceptance Scenarios**:

1. **Given** any agreed page, **When** shared navigation is used, **Then** Home, About the doctor,
   Services, and Contact are reachable, with the current destination identifiable.
2. **Given** a narrow or wide viewport, **When** navigation and content are read, **Then** text,
   portraits, controls, and the map do not overlap, become clipped, or require page-wide horizontal
   scrolling at the accessibility reflow test width.
3. **Given** keyboard-only interaction, **When** controls receive focus and are activated,
   **Then** focus is visible, order is logical, and no keyboard trap occurs.
4. **Given** Home, **When** Our Services is activated, **Then** Services opens without a dead link.

### Edge Cases

- A map is blocked or never finishes loading: essential contact information stays independent
  of the embed; no requirement assumes reliable detection of a third-party failure.
- A portrait is unavailable: preserve doctor identification and usable layout, not the reference's
  developer-facing image-placeholder instructions.
- A long qualification, phone number, or address wraps on small screens: keep its full meaning
  visible, legible, and available without overlap.
- Browser zoom and text enlargement: navigation and content remain usable under WCAG reflow
  and text-resizing checks.
- A device cannot place calls: both numbers remain readable for manual dialing on another device;
  the site must not report a call or booking as completed.
- The appointment popup is part of the confirmed experience. It MUST open from the shared top
  banner on all four pages, work by keyboard, have an accessible name, manage focus on opening,
  dismiss with Escape and a labeled close control, and return focus to its trigger when closed.
- Copy icons MUST be controls with accessible names identifying which number they copy and give success or
  failure feedback. If copying is unavailable, each number MUST remain selectable for manual copy.
- No form, authenticated workflow, or user-entered-data recovery state is needed in this scope;
  do not invent such features to satisfy generic template examples.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Provide the four agreed pages and consistent, keyboard-operable navigation between
  them; each page MUST also be directly reachable. Acceptance: Story 5 scenarios 1 and 3.
- **FR-002**: Home MUST preserve the supplied introduction, three highlights, portrait, and
  Our Services destination, with appointment wording corrected to phone-only. Acceptance: Story 3
  scenario 1 and Story 5 scenario 4.
- **FR-003**: About MUST preserve all supplied profile, qualification, experience, specialization,
  and academic/research content, including the distinction between current and past procedures.
  Acceptance: Story 3 scenarios 2 and 3.
- **FR-004**: Services MUST show only the three supplied service descriptions; remove all
  "Learn more" controls without replacement actions or detail pages. Acceptance: Story 4.
- **FR-005**: Contact MUST show the supplied address, two reception numbers, consultation hours,
  and named map embed. Written contact information MUST remain usable independently of the map.
  Acceptance: Story 1 scenario 1 and Story 2.
- **FR-006**: Appointment information MUST show both confirmed numbers and explain telephone
  booking; it MUST NOT imply that the site books or confirms appointments. Acceptance: Story 1.
- **FR-007**: A shared top banner on all four pages MUST contain a visible "Book Appointment"
  button. Activating it MUST open a popup with both confirmed numbers and a telephone-booking
  instruction. Acceptance: Story 1 scenario 3.
- **FR-008**: Each number in the popup MUST have a labeled copy icon control. Successful copying MUST
  provide success feedback; denied or unavailable clipboard access MUST provide clear failure
  feedback while leaving the number visible and selectable. Acceptance: Story 1 scenarios 4-5.
- **FR-009**: Use landing_page_hero.jpeg for the Home hero and about_page.jpeg for About; preserve
  aspect ratio and recognizable facial framing, with descriptive alternative text and usable
  failure behavior. Do not use obsolete image paths. Acceptance: Story 3 and visual asset checks.
- **FR-010**: Preserve useful reference composition, section order, visual hierarchy, content,
  and responsive intent, except for confirmed overrides and accessibility corrections. Do not
  silently change content meaning. Acceptance: page-by-page comparison with the four reference
  sections, including all qualifications, experience entries, and six academic/research figures.
- **FR-011**: Target WCAG 2.2 AA across all four pages and the appointment popup,
  including keyboard access, visible/unobscured focus, clear names and labels, semantic headings,
  readable contrast, text resizing, reflow, and applicable target-size requirements. The popup
  MUST return focus to its trigger when closed. Acceptance: accessibility review plus Story 5
  and popup tests.
- **FR-012**: Content MUST remain readable on mobile and desktop without incoherent overlaps,
  clipped controls, distorted portraits, or hidden contact information. Acceptance: Story 5
  scenario 2 and manual responsive checks.
- **FR-013**: The website MUST NOT solicit, collect, or store patient names, phone numbers,
  appointment details, or health information. Reception's manual process stays outside the site.
  Acceptance: all-page inspection and data-flow review confirm no patient-entry controls,
  submission paths, or patient storage.
- **FR-014**: No digital booking, accounts, staff tools, invented backend integrations, additional
  analytics/tracking, or compliance claims may be introduced. The supplied map is the only agreed
  external integration. Acceptance: scope, content, and external-request review.
- **FR-015**: Unavailable media MUST NOT prevent reading the page or finding contact information;
  do not expose sensitive data, internal errors, or developer instructions in public feedback.
  Acceptance: image failure and map-blocked tests from Stories 2 and 3.
- **FR-016**: Delivery MUST include automated regression checks for navigation, required content,
  both phone numbers, asset placement, removed/unsupported actions, and applicable media-failure
  behavior; supplement them with manual keyboard, responsive, and accessibility checks. Record
  actual results and limitations, not claims of unperformed testing.
- **FR-017**: Delivery MUST document prerequisites, agreed setup, environment variables with safe
  placeholders, and exact run/test commands. Acceptance: a reviewer follows the documentation
  from a clean development setup and records the results without using committed secrets.

### Explicit Exclusions

No public appointment form, calendar, availability service, booking integration or confirmation;
no patient accounts, staff dashboard, appointment management, or patient records; no service-detail
pages or replacement service actions; no unapproved pages, integrations, tracking, testimonials,
medical claims, services, or statistics. A possible appointment page is not approved by listing
it as an option. No claim of legal/regulatory compliance is authorized.

### Confirmed Delivery Constraints

The constitution requires Django/Python, Django Templates, and Tailwind CSS. React is a reference,
not a runtime requirement. VS Code extensions are not runtime dependencies. These are supplied
constraints, not newly proposed implementation details; project structure, versions, build tooling,
and detailed implementation belong in planning, not this specification.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All four pages are reachable directly and through shared navigation in desktop,
  mobile, and keyboard-only acceptance checks, with no broken navigation destinations.
- **SC-002**: From each of the four pages, visitors can open the shared appointment popup and find
  both confirmed numbers and an explicit telephone-booking instruction without entering patient
  data; each number can be copied or manually selected if clipboard access fails.
- **SC-003**: A reference comparison accounts for every supplied content section on the four
  pages, the three services, and both correctly assigned portraits; every difference is an
  approved override or documented accessibility correction.
- **SC-004**: All four pages contain zero Services "Learn more" controls, online-booking claims,
  patient-entry forms, or links implying an implemented online appointment workflow; the shared
  "Book Appointment" control opens only the confirmed telephone-number popup.
- **SC-005**: At 320 CSS pixels (the WCAG reflow test width), a representative wider mobile width,
  and a desktop width recorded in the test report, all four pages retain complete readable content
  without unintended page-wide horizontal scrolling, overlapping text, or obscured controls.
- **SC-006**: Manual keyboard and accessibility checks find no unresolved applicable WCAG 2.2 AA
  failures before acceptance; automated checks supplement rather than certify this review.
- **SC-007**: With either portrait unavailable and with the map blocked, visitors can still identify
  the doctor and read the complete address, hours, and both phone numbers.
- **SC-008**: Required regression checks pass, and a reviewer can reproduce documented run/test
  commands; actual results and any remaining limitations are recorded before acceptance.

## Assumptions

### Repository Evidence

- Sources inspected: ../../.specify/memory/constitution.md (v1.1.0), all of ../../oldui.txt,
  ../../landing_page_hero.jpeg, and ../../about_page.jpeg.
- The text provides four UI snippets, not a runnable old application or screenshots. Existing
  backend behavior, a shared header implementation, and appointment functionality are unverified.
- Both portraits were visually inspected; their assigned page roles come from owner confirmation,
  not identity inference from the images or obsolete source filenames.
- The old Home wording promises online booking and links to /appointment. Those details are
  explicitly overridden by phone-only booking. The old service buttons are explicitly removed.
- The constitution's summary comment still calls service behavior deferred; its confirmed-decision
  body and this request resolve that issue as removal. No constitution edit is made by this command.

### Owner-Confirmed Decisions

- The four pages, phone-only booking, manual reception process, no online patient-data collection,
  delivery stack, portrait mapping, and removal of service actions are agreed.
- Medical claims, contact details, hours, and the supplied map destination are owner-confirmed as
  accurate and unchanged, not independently verified or assessed for legal compliance.
- The source currently lists the landline as +91 080 2653 4899. Preserve that published wording;
  no unverified dialing normalization is required by this specification.

### Dependencies and Confirmed Decisions

- The shared-banner appointment popup and per-number copy controls are owner-confirmed by the
  2026-10-21 clarification. No dedicated appointment page or online booking flow is in scope.
- The supplied portraits and approved reference copy are delivery inputs. The embedded map
  depends on an external provider; core contact information must not depend on its availability.
- Tests define verifiable behavior, not a claimed working implementation. No traffic targets,
  hosting provider, database, authentication system, or new runtime integration is assumed.