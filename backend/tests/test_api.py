import pytest
from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"question": "What are SEC filing requirements?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert "entities" in response.json()

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}