# Dhanush Flask App

Run locally (development):

```bash
python app.py
```

Run as a simple production server on Windows using Waitress:

```bash
pip install -r requirements.txt
waitress-serve --listen=*:10000 app:app
```

Run on Heroku / Linux with Gunicorn:

```bash
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:10000
```

Procfile (for Heroku): `web: gunicorn app:app`

Notes:
- In production, keep `debug=False`.
- Use a process manager (systemd, Supervisor, Heroku dynos, or Windows service) to restart on crashes.

Windows: keep the site running 24/7 using a Scheduled Task

1. Ensure Python is installed and the `py` launcher is available.
2. From an elevated PowerShell (Run as Administrator) in the project folder run:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\create_schtask.ps1
```

What this does:
- `run_waitress.bat` installs any missing requirements and starts the app with `waitress`.
- `create_schtask.ps1` registers `run_waitress.bat` to run at system startup so the app starts automatically when Windows boots. This keeps the site running after you close VS Code.

If you prefer a Windows Service instead of a scheduled task, install NSSM (Non-Sucking Service Manager) and point it at `run_waitress.bat`.
