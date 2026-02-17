from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check_success():
    """
    Test that the /health endpoint returns 200 OK,
    the correct status message, and a timestamp.
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "timestamp" in data

def test_health_details_success():
    """
    Test that /health/details returns system stats.
    """
    response = client.get("/health/details")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "system" in data
    assert "cpu_percent" in data["system"]
    assert "memory_percent" in data["system"]
