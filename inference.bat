@echo off
setlocal

:: Check if virtual environment exists and activate it
if exist venv\Scripts\activate (
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate
)

:: Run inference
:: Usage: inference.bat "Your message here"
if "%~1"=="" (
    echo [INFO] Running example inference...
    python scripts/inference.py --config configs/inference.yaml
) else (
    echo [INFO] Running inference for: "%~1"
    python scripts/inference.py --config configs/inference.yaml --message "%~1"
)

if %errorlevel% neq 0 (
    echo [ERROR] Inference failed.
)

pause
