<!--
Sync Impact Report
Version change: 1.0.0 -> 1.1.0 (expanded evidence guidance and resolved Django direction).
Modified principles: II. Evidence-Based Requirements (UI evidence is not backend proof);
V. Clear Frontend/Backend Responsibilities (Django/Python required by updated reference;
React is reference-only, not a required runtime).
Updated section: Evidence and Open Questions, based on the now-populated oldui.txt.
Added sections: none. Removed sections: none.
Dependent templates and commands: unchanged; they read this constitution at runtime.
Deferred clarifications: booking and service-detail behavior, shared navigation and staff scope,
styling/template approach, image mapping, publication accuracy, and data/access requirements.
No template placeholders remain. Ratification date preserved.
-->

# GGS Medical Clinic Constitution

## Core Principles

### I. User Workflows First

Design around agreed tasks for clinic visitors and staff. Preserve workflows verified in the
old UI unless an explicit change is approved. Every feature MUST trace to a confirmed need
or an agreed proposal; do not invent screens, features, wording, or workflows to fill gaps.

### II. Evidence-Based Requirements

Inspect available UI source, screenshots, documentation, and project files before making
decisions. Requirements MUST distinguish repository facts, assumptions, and proposed decisions,
with references for facts. Record missing or incomplete evidence and obtain clarification of
important ambiguities before implementing affected behavior; never present inference as fact.
UI reference code establishes supplied design and content, not working integrations, backend
contracts, authorization, or the accuracy of medical and contact claims.

### III. Privacy and Security

Treat health and personal information as sensitive. Collect only data necessary for an agreed
workflow, enforce least-privilege access on the server, and keep secrets out of source control.
Logs and error messages MUST NOT expose sensitive information. Legal or regulatory compliance
MUST NOT be claimed without confirmed requirements and appropriate review.

### IV. Accessible, Responsive Interface

Pages MUST work on mobile and desktop, with keyboard-operable controls, clear labels, visible
focus, readable text, and sufficient contrast. Target WCAG 2.2 AA unless a different standard
is explicitly agreed and documented. Verify affected workflows for accessibility and responsive
layout rather than relying on appearance alone.

### V. Clear Frontend/Backend Responsibilities

Use Django/Python, as directed by `oldui.txt`, and translate the supplied React UI reference
without requiring React as an application runtime. Keep browser presentation and interaction
separate from server-side business rules, data access, validation, and authorization. Do not
infer backend connections from the reference code. Confirm the Django rendering approach and
styling tools before scaffolding; Tailwind-style classes in a reference do not by themselves
approve Tailwind CSS as a dependency. VS Code extensions are development tools, never runtime
dependencies.

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

Current evidence: `oldui.txt` supplies React UI snippets for Home, About, Services, and Contact,
and explicitly requests translation to Django/Python for UI purposes, not reuse of backend
connections. It records reference layout, copy, service listings, contact details, hours, a
map embed, and links to `/appointment` and `/services`. Preserve these as the design/content
baseline unless an explicit change is agreed; their presence does not prove production behavior
or factual accuracy. `landing_page_hero.jpeg` and `about_page.jpeg` are portrait assets, not
rendered UI screenshots. No runnable application or runtime dependency manifest is available.

Resolve the following before implementing the affected scope:

- What must the appointment links do? No appointment page, form, confirmation, availability,
	or booking integration is supplied. Service "Learn more" buttons have no defined action.
- What shared navigation, remaining screens, and staff workflows, if any, are in scope?
	These are not supplied; request references or explicit decisions before implementing them.
- Which Django rendering approach and styling tools are agreed? Tailwind CSS remains unconfirmed.
- Do the supplied portraits map to the reference paths `/gg_shetty_pic.jpeg` and
	`/gg_shetty2_pic.jpeg`? Confirm asset use and verify medical claims, contact details, hours,
	and the embedded map destination before publication.
- Will any agreed workflow collect personal or health information? If so, confirm necessary
	fields, access roles, retention/deletion rules, and applicable legal/review requirements.

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
