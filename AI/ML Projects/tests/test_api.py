from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200


def test_predict():
    payload = {
        "age": 50,
        "gender": 1,
        "num_procedures": 2,
        "num_medications": 10,
        "time_in_hospital": 5
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "readmission_risk" in response.json()