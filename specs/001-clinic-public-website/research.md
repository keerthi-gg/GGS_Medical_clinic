# Research: GGS Medical Clinic Public Website

**Date**: 2026-10-21
**Scope**: Resolve technical choices needed to plan the server-rendered four-page site. Product
decisions remain those recorded in [spec.md](spec.md).

## Decisions

### Django and Python Baseline

**Decision**: Use Django 6.1 with Python 3.12 or newer, then pin the exact compatible dependency
set in the project files during setup.

**Rationale**: The official Django 6.1 tutorial states that this release supports Python 3.12 and
later. The workspace contains no Python version declaration, environment, dependency manifest, or
Django project, so actual interpreter availability must be checked before setup. Do not claim
that this repository already runs Django.

**Alternatives considered**: Select a legacy Django/Python combination without repository
evidence; reject because it increases maintenance risk. Pin a precise patch release now; defer
until the chosen interpreter and package resolver are available so the lock records a compatible,
reproducible set.

### Tailwind CSS Delivery

**Decision**: Use the Tailwind CSS CLI to scan Django HTML templates and compile one CSS file into
Django's namespaced static assets. Keep the CLI and npm package development/build-time only.

**Rationale**: Tailwind's official CLI guide describes scanning source files and writing generated
CSS to a static output file, which fits Django Templates without adding React or a frontend bundler.
Django's static-files guide supports app-namespaced static assets and template URL generation via
the `static` template tag. Production serving remains the deployment host's responsibility and is
not selected in this feature plan.

**Alternatives considered**: Tailwind Play CDN; rejected for the delivered site because compiled
static CSS is more appropriate for production than a development-oriented CDN. A React/Vite build;
rejected because React is reference-only and server-rendered templates are confirmed. A standalone
Tailwind executable could avoid Node.js, but npm's CLI package plus lockfile is easier to reproduce
with project scripts; confirm Node.js availability during setup.

### Appointment Popup

**Decision**: Use a labeled native HTML `<dialog>` opened modally, with an explicit close button,
copy icon controls, and browser-side feedback. Verify keyboard behavior and focus return in real
browsers and assistive-technology review.

**Rationale**: MDN documents `showModal()` as providing modal behavior, making the rest of the
document inert, moving initial focus, and supporting Escape dismissal. WAI-ARIA APG specifies a
dialog label, focus containment, Escape behavior, a visible close control, and returning focus to
the invoking control. Native semantics reduce custom behavior while still requiring acceptance
testing against the spec.

**Alternatives considered**: A custom div with ARIA; rejected because it requires recreating modal
focus and inertness behavior. A non-modal popover; rejected because the agreed experience is a popup
used to focus appointment contact and the spec requires modal dialog keyboard behavior.

### Copy Number Interaction

**Decision**: Use the browser Clipboard API from a user-activated copy icon. On success, announce
which number was copied; on failure or unavailable clipboard access, show a clear message and leave
the phone number visible and selectable for manual copying.

**Rationale**: MDN documents `Clipboard.writeText()` as asynchronous, restricted to secure contexts,
and capable of rejecting with `NotAllowedError`. The spec already requires success/failure feedback
and manual selection fallback. The deployed site must use HTTPS for clipboard support; local
development should use localhost.

**Alternatives considered**: Assume clipboard access always succeeds; rejected because browser
permissions and secure-context rules make that unreliable. Add an external clipboard library;
unnecessary for a single text-copy interaction.

### Automated and Manual Testing

**Decision**: Use Django's built-in test runner for page response, route, and rendered-content
checks. Add pytest with the official Playwright pytest plugin for browser-level behavior and media
failure checks. Preserve manual keyboard, responsive, and WCAG 2.2 AA review as separate gates.

**Rationale**: Django documents its test framework for simulated requests and rendered output.
Playwright recommends its pytest plugin for end-to-end browser tests and supports Chromium,
Firefox, and WebKit. Browser tests are needed for dialog interaction, copy success/failure, image
load failure, map blocking, and layout at specified viewports; Django's request client alone cannot
verify these browser behaviors.

**Alternatives considered**: Django tests only; rejected because they do not exercise browser
interaction or responsive rendering. Manual-only UI review; rejected because required page,
content, and regression checks should be repeatable. A JavaScript framework; unnecessary because
the UI is server-rendered and needs only small vanilla browser behavior.

## Verified Repository Facts

- The repository contains the clarified spec, constitution, `oldui.txt`, and two JPEG portraits;
  it has no `manage.py`, application package, dependency manifests, README setup, tests, or lockfiles.
- The spec resolves appointment presentation to a shared top-banner button and number-copy dialog.
- No extension hooks are configured in `.specify/extensions.yml`.

## Official References

- [Django 6.1 tutorial and Python compatibility](https://docs.djangoproject.com/en/6.1/intro/tutorial01/)
- [Django static files](https://docs.djangoproject.com/en/6.1/howto/static-files/)
- [Django testing](https://docs.djangoproject.com/en/6.1/topics/testing/)
- [Django deployment checklist](https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/)
- [Tailwind CSS CLI installation](https://tailwindcss.com/docs/installation/tailwind-cli)
- [MDN: HTML dialog element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
- [WAI-ARIA APG: Modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [MDN: Clipboard.writeText](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText)
- [Playwright for Python: installation](https://playwright.dev/python/docs/intro)