# Start Backend
Start-Process -FilePath ".\venv\Scripts\python.exe" -ArgumentList "run.py" -NoNewWindow

# Wait for backend to initialize
Write-Host "Waiting for backend to start..."
Start-Sleep -Seconds 5

# Start Frontend
Write-Host "Starting Streamlit frontend..."
.\venv\Scripts\streamlit.exe run frontend/app.py
