@echo off

:: 1) Check if already running as admin:
net session >nul 2>&1
if %errorLevel% neq 0 (
  echo Requesting admin privileges...
  powershell -Command "Start-Process '%~f0' -Verb RunAs"
  goto :eof
)

:: 2) If we're here, we have admin. Now run your script:
start "" pythonw C:\Users\Henry\Desktop\flash\flash_timer.py
exit