# Create a scheduled task to run the `run_waitress.bat` at system startup.
# Must be run as Administrator.

$taskName = "DhanushApp"
$scriptPath = Join-Path $PSScriptRoot "run_waitress.bat"

Write-Host "Creating scheduled task '$taskName' to run:`n $scriptPath`n"

if (-not (Test-Path $scriptPath)) {
    Write-Error "run_waitress.bat not found at $scriptPath"
    exit 1
}

# Use schtasks to create a task that runs at system startup as the current user.
$cmd = "schtasks /Create /SC ONSTART /TN $taskName /TR `"$scriptPath`" /RL HIGHEST /F"

Write-Host "Running: $cmd"
Invoke-Expression $cmd

Write-Host "Task created. If you want it to run at logon instead, re-run with /SC ONLOGON."
