# GGS Medical Clinic Website

Informational clinic website using Django Templates and Tailwind CSS. The UI code in `oldui.txt`
is reference-only; it does not represent backend behavior.

## Prerequisites

- Python 3.12 or newer
- Node.js and npm

## Local Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
npm ci
python -m playwright install chromium
```

If PowerShell blocks activation, use a process-scoped execution policy or invoke `.venv\Scripts\python.exe` directly. Do not change the machine-wide execution policy for this project.

## Run and Validate

```powershell
npm run css:build
python manage.py check
python manage.py test
python -m pytest
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the local site. The Django development server is not for
production. Browser clipboard copying requires a secure context; localhost is treated as secure
by supported browsers, and production must use HTTPS.

## Scope and Privacy

Appointments are booked by phone using the two published clinic numbers. The website does not
collect patient information, accept booking requests, or provide staff appointment management.
The Google Maps embed is the only external integration currently in scope. No real secrets are
needed for local development; keep `DJANGO_SECRET_KEY` unset locally or supply a private value
through the environment for non-local deployments. Never commit secret values.