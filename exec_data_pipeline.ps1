Write-Host "🔄 Starting Data Pipeline..."

# Ativar virtualenv (se existir)
if (Test-Path "venv\Scripts\Activate.ps1") {
    & "venv\Scripts\Activate.ps1"
    Write-Host "✅ Virtual environment activated"
} else {
    Write-Host "⚠️ Virtual environment not found. Running without it."
}

# Executar pipeline
python main.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Pipeline executed successfully"
} else {
    Write-Host "❌ Pipeline execution failed"
}
