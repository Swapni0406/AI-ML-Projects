# Hospital Readmission Prediction Pipeline

## Overview
Production-grade ML pipeline to predict hospital readmission risk.

## Features
- XGBoost model
- FastAPI inference API
- Dockerized deployment
- CI/CD with GitHub Actions
- Unit testing with PyTest
- PEP8 compliant code

## Run Locally

### Train Model
python src/models/train.py

### Start API
uvicorn app.main:app --reload

### Docker
docker build -t readmission-api .
docker run -p 8000:8000 readmission-api