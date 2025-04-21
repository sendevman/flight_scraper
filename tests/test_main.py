from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_flight_search():
    response = client.get("/api/flight?airline_code=AA&flight_number=100&departure_date=2025-04-19")
    assert response.status_code == 200
    assert "flight_number" in response.json()