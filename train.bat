@echo off
setlocal

:: Check if virtual environment exists and activate it
if exist venv\Scripts\activate (
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate
)

echo [STEP 1] Preprocessing data...
python scripts/preprocess_data.py --train_size 1000 --test_size 200
if %errorlevel% neq 0 (
    echo [ERROR] Preprocessing failed.
    pause
    exit /b %errorlevel%
)

echo [STEP 2] Training the model with Unsloth...
python scripts/train.py --config configs/train.yaml
if %errorlevel% neq 0 (
    echo [ERROR] Training failed.
    pause
    exit /b %errorlevel%
)

echo [SUCCESS] Training completed!
pause
