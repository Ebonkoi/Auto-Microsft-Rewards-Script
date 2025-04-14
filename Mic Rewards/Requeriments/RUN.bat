@echo off
:: Set to the directory where the script is located
cd /d "%~dp0"

echo Installing Python...

:: Check if Python is already installed
if exist "%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe" (
    echo Python is already installed. Skipping installation...
    goto :run_python_script
)

:: Install Python with Winget
winget install Python.Python.3.11 -e --silent
if %errorlevel% neq 0 (
    echo Error installing Python! Make sure Winget is updated.
    pause
    exit /b
)

:: Add Python to PATH
set "PYTHON_PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python311"
set "PYTHON_SCRIPTS=%PYTHON_PATH%\Scripts"
set "PATH=%PYTHON_PATH%;%PYTHON_SCRIPTS%;%PATH%"

:: Verify that Python installation was successful
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python was not found in the PATH! Please reset the prompt manually and try again.
    pause
    exit /b
)

:run_python_script
echo Starting requeriments.py
python requeriments.py

:: Close script if has no error
if %errorlevel% equ 0 exit
pause