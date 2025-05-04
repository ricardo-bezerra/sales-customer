<h1 align="center">📊 Data Ingestion Pipeline</h1>

<p align="center">A robust pipeline for ingesting, cleaning, and exporting customer data in CSV, JSON and Parquet formats.</p>

---

### 🚀 Features

- Reads raw `.csv` files
- Cleans and standardises data (names, emails, ages)
- Outputs in:
  - CSV
  - JSON
  - Parquet (Snappy)
- Uses `self` parameters in a dedicated config class
- Modular structure with OOP
- Executable via PowerShell on Windows

---

### 📁 Project Structure


# =============================================================================== #


### Build and execution by Docker

## 1. Container creation:
## bash
# docker build -t data-pipeline .

## 2. Pipeline execution:
## bash
# docker run --rm data-pipeline
