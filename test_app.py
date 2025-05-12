from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json()["model_type"] == "LinearRegression"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_prediction():
    response = client.post("/predict", json={"value": 3})
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], float)

def test_config_env_var(monkeypatch):
    monkeypatch.setenv("MY_CONFIG_VALUE", "Test123")
    response = client.get("/config")
    assert response.status_code == 200
    assert response.json() == {"config": "Test123"}
