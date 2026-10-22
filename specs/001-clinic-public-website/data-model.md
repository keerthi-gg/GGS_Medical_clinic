# Data Model: GGS Medical Clinic Public Website

## Decision

No application data model is needed for this feature.

The site presents owner-approved clinic information and does not create, receive, or retain
patient records, appointment requests, user accounts, staff records, or submissions. A database
entity for patients or appointments would violate the confirmed scope. Keep the approved copy,
phone numbers, and asset references as presentation content; do not add persistence or migrations
for them.

The Django project's own configuration and any framework-internal defaults are not clinic domain
entities. During implementation, disable unused admin/authentication or other features rather than
creating staff workflows that are not in scope.

## Validation

- Confirm no application models or patient/appointment tables are introduced.
- Confirm all pages render with the approved public content without submitted user data.
- Review settings and dependencies for unused data-backed features before acceptance.