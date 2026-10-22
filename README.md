# GGS Medical Clinic Website

Informational clinic website using Django Templates and Tailwind CSS. The UI code in `oldui.txt`
is reference-only; it does not represent backend behavior.

## Prerequisites

- Python 3.12 or newer
- Node.js and npm

## Local Setup

Run the commands from the project directory. Python 3.12 or newer and Node.js with npm must be installed.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
npm ci
python -m playwright install chromium
```

If PowerShell blocks activation, allow scripts for this terminal session with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`, then activate the environment again. Alternatively, use `.venv\Scripts\python.exe` directly. Do not change the machine-wide execution policy for this project.

### macOS (Terminal)

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
npm ci
python -m playwright install chromium
```

If npm reports that `@parcel/watcher` has an install script not covered by `allowScripts`, the CSS build may still work without approval. Only if a command fails because that package's script was blocked, review and approve it with `npm approve-scripts @parcel/watcher`.

## Run and Validate

With the virtual environment activated, these commands work on both platforms:

```sh
npm run css:build
python manage.py check
python manage.py test
python -m pytest
python manage.py runserver
```

On Windows, activate with `\.venv\Scripts\Activate.ps1`; on macOS, activate with `source .venv/bin/activate`. Keep the terminal running while using the site.

Open `http://127.0.0.1:8000/` for the local site. The Django development server is not for
production. Browser clipboard copying requires a secure context; localhost is treated as secure
by supported browsers, and production must use HTTPS.

## Scope and Privacy

Appointments are booked by phone using the two published clinic numbers. The website does not
collect patient information, accept booking requests, or provide staff appointment management.
The Google Maps embed is the only external integration currently in scope. No real secrets are
needed for local development; keep `DJANGO_SECRET_KEY` unset locally or supply a private value
through the environment for non-local deployments. Never commit secret values.