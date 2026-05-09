# Ask to run Ex2 Training Pipeline First
$runEx2 = Read-Host "Do you want to run the Ex2 training pipeline first to generate the intent model? (y/n)"
if ($runEx2 -match "^[yY]$") {
    Write-Host "--- Running Ex2 Training Pipeline ---"
    Set-Location -Path "..\Ex2"

    Write-Host "1. Preprocessing Data..."
    python scripts/preprocess_data.py --train_size 1000 --test_size 200

    Write-Host "2. Training Intent Model..."
    python scripts/train.py --config configs/train.yaml

    Write-Host "✅ Ex2 Training Complete. Returning to Ex3..."
    Set-Location -Path "..\Ex3"
} else {
    Write-Host "⏭️ Skipping Ex2 training..."
}

# Start Backend
Write-Host "Starting FastAPI Backend..."
Start-Process -FilePath ".\venv\Scripts\python.exe" -ArgumentList "run.py" -NoNewWindow

# Wait for backend to initialize
Write-Host "Waiting for backend to start..."
Start-Sleep -Seconds 5

# Start Frontend
Write-Host "Starting Streamlit frontend..."
.\venv\Scripts\streamlit.exe run frontend/app.py
