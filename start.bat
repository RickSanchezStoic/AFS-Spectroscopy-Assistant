@echo off
echo AFS Spectroscopy Assistant
echo ==========================
if "%ANTHROPIC_API_KEY%"=="" (
    set /p ANTHROPIC_API_KEY="Enter your Anthropic API key: "
)
set FLASK_ENV=development
C:\Users\Risha\AppData\Local\Programs\Python\Python39\python.exe app.py
pause
