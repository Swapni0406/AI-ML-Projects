from fastapi import FastAPI
from app.model_loader import load_model
from app.schema import PatientData
import numpy as np

app = FastAPI(title="Hospital Readmission API")

model = load_model()


@app.get("/")
def health_check():
    return {"status": "OK"}


@app.post("/predict")
def predict(data: PatientData):
    input_data = np.array([list(data.dict().values())])
    prediction = model.predict_proba(input_data)[0][1]

    return {"readmission_risk": float(prediction)}