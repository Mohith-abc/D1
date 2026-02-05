#!/usr/bin/env pwsh
# Checks http://127.0.0.1:10000 and starts run_waitress.bat if the site is down.
$uri = 'http://127.0.0.1:10000/'
Write-Host "Checking $uri ..."
try {
    $resp = Invoke-WebRequest -Uri $uri -UseBasicParsing -TimeoutSec 3
    Write-Host "Server is UP (HTTP $($resp.StatusCode))."
    exit 0
} catch {
    Write-Host "Server is DOWN. Attempting to start run_waitress.bat..."
}

$bat = Join-Path $PSScriptRoot 'run_waitress.bat'
if (-not (Test-Path $bat)) {
    Write-Error "run_waitress.bat not found at $bat"
    exit 2
}

Start-Process -FilePath $bat -WorkingDirectory $PSScriptRoot -WindowStyle Hidden
Write-Host "Started run_waitress.bat (detached). Waiting 4s to verify..."
Start-Sleep -Seconds 4
try {
    $resp = Invoke-WebRequest -Uri $uri -UseBasicParsing -TimeoutSec 5
    Write-Host "Server STARTED (HTTP $($resp.StatusCode))."
    exit 0
} catch {
    Write-Error "FAILED to start server. Check run_waitress.bat output or logs."
    exit 3
}
