<!--
Sync Impact Report
Version change: 1.0.0 -> 1.1.0 (expanded guidance and confirmed project decisions).
Modified principles: I. User Workflows First (phone-only booking and manual staff process);
III. Privacy and Security (no online patient-data collection);
V. Clear Frontend/Backend Responsibilities (Django Templates and Tailwind CSS confirmed).
Updated section: Evidence and Open Questions (UI reference, owner confirmations, asset mapping).
Added sections: none. Removed sections: none.
Dependent templates and commands: unchanged; they read this constitution at runtime.
Deferred clarifications: appointment contact presentation and service "Learn more" behavior.
No template placeholders remain. Original ratification date preserved.
-->

# GGS Medical Clinic Constitution

## Core Principles

### I. User Workflows First

Design around agreed tasks for clinic visitors and staff. Preserve workflows verified in the
old UI unless an explicit change is approved. Every feature MUST trace to a confirmed need
or an agreed proposal; do not invent screens, features, wording, or workflows to fill gaps.
Booking MUST be by telephone using the two published clinic numbers, not a digital calendar
or public booking form. The receptionist's manual recording of patient names, phone numbers,
and appointment times is outside the website; do not add staff software for this process.

### II. Evidence-Based Requirements

Inspect available UI source, screenshots, documentation, and project files before making
decisions. Requirements MUST distinguish repository facts, assumptions, and proposed decisions,
with references for facts. Record missing or incomplete evidence and obtain clarification of
important ambiguities before implementing affected behavior; never present inference as fact.

### III. Privacy and Security

Treat health and personal information as sensitive. Collect only data necessary for an agreed
workflow, enforce least-privilege access on the server, and keep secrets out of source control.
Logs and error messages MUST NOT expose sensitive information. Legal or regulatory compliance
MUST NOT be claimed without confirmed requirements and appropriate review.
The initial website MUST NOT solicit, collect, or store patient names, phone numbers, appointment
details, or health information online. The manual telephone process does not authorize online
data collection. Any future expansion requires explicit approval and a privacy/security review.

### IV. Accessible, Responsive Interface

Pages MUST work on mobile and desktop, with keyboard-operable controls, clear labels, visible
focus, readable text, and sufficient contrast. Target WCAG 2.2 AA unless a different standard
is explicitly agreed and documented. Verify affected workflows for accessibility and responsive
layout rather than relying on appearance alone.

### V. Clear Frontend/Backend Responsibilities

Use Django/Python with Django Templates for HTML structure and Tailwind CSS for styling.
The React code in `oldui.txt` is a UI reference, not a required runtime or a backend contract.
Keep browser presentation and interaction separate from server-side business rules, data access,
validation, and authorization where applicable. Do not invent backend integrations or patient
storage for this informational site. VS Code extensions are development tools, never application
runtime dependencies.

### VI. Maintainable, Testable Changes

Prefer small, understandable components and modules with clear responsibilities. Changes MUST
include tests for affected important workflows, validation rules, permissions, and regressions.
Keep changes scoped to the agreed feature; unrelated refactoring or fixes require separate
agreement. Template examples or optional-test wording do not waive these testing requirements.

### VII. Reliable Errors and Loading

Provide clear loading, empty, success, and error feedback wherever those states apply.
Validate data on the server even when the UI also validates it. Failed operations MUST preserve
user-entered information for correction or retry without insecure persistence of sensitive data.
Errors MUST be actionable without exposing private data or internal implementation details.

### VIII. Documentation and Project Setup

Document the agreed development setup, prerequisites, environment variables, and exact commands
to run and test the application. Update instructions when setup changes and verify that they
work. Example configuration MUST use safe placeholders, never real secrets or personal data.

## Evidence and Open Questions

Repository evidence: `oldui.txt` supplies React UI snippets for Home, About, Services, and
Contact and directs their translation to Django/Python for UI purposes, not backend reuse.
It is the design/content baseline, not proof of working integrations. The two JPEGs are portrait
assets, not rendered UI screenshots. No runnable application or runtime dependency manifest
is present in the inspected repository.

Project-owner decisions confirmed on 2026-10-20:

- Agreed navigation: Home, About the doctor, Services, and Contact. Booking is by telephone;
	display both reception/booking numbers from the reference: +91 99459 88815 and
	+91 080 2653 4899. Do not infer an online booking workflow from the old `/appointment` links.
- The receptionist receives calls and manually records names, phone numbers, and appointment
	times. No patient-data entry, staff dashboard, or digital appointment management is in scope.
- Django Templates and Tailwind CSS are confirmed; React is reference-only.
- Use `landing_page_hero.jpeg` in the Home hero and `about_page.jpeg` on the About page.
	The old `/gg_shetty_pic.jpeg` and `/gg_shetty2_pic.jpeg` paths MUST NOT be reused.
- The owner confirms the reference medical claims, contact details, hours, and embedded map
	destination are accurate and unchanged. This is owner confirmation, not independent verification
	or a legal/regulatory compliance assessment.
-  What must the Services "Learn more" buttons do -  they must be removed. No action is supplied.

Remaining decisions to resolve before implementing the affected UI:

- How will appointment contact information be presented: prominently on Home, in a dedicated
	section/page, or through a persistent header button opening a popup with both numbers?
	These are alternatives, not approved additional pages or controls; do not choose silently.

Record answers and their evidence in the relevant specification or decision record. An open
question is not authorization to choose a default or implement an unapproved capability.

## Development and Review Gates

- Before implementation, specifications MUST identify approved workflows, supporting evidence,
	explicit assumptions, and resolved decisions that affect scope, architecture, or sensitive data.
- Plans and task lists MUST apply this constitution, including required tests and relevant
	privacy, accessibility, responsive-layout, validation, and failure-state checks.
- Before acceptance, reviewers MUST verify the agreed behavior, relevant passing tests, manual
	keyboard/mobile/desktop checks for UI changes, and updated run/test documentation. Record
	limitations and resolve blocking failures; do not claim unperformed checks passed.

## Governance

This constitution takes precedence over conflicting template examples and project practices.
Specifications, plans, tasks, and reviews MUST check compliance. A conflicting change MUST be
revised or receive an approved constitutional amendment before implementation.

Amendments MUST document the reason, impact on existing work, and any migration needed, receive
project-owner approval, and update the version, amendment date, and Sync Impact Report. Use
semantic versioning: MAJOR for incompatible principle changes/removals, MINOR for new or
materially expanded guidance, PATCH for non-semantic clarifications. Preserve the original
ratification date. Version 1.0.0 establishes the initial constitution requested for this project.

**Version**: 1.1.0 | **Ratified**: 2026-10-20 | **Last Amended**: 2026-10-20
