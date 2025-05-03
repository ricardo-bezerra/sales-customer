# Base image
FROM python:3.10-slim

# Metadata
LABEL maintainer="seu-email@exemplo.com"
LABEL description="Data ingestion pipeline with cleaning, transformation and export"

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the app code
COPY app/ ./app/
COPY files/ ./files/

# Entry point
CMD ["python", "app/main.py"]
