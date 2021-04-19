import json


def test_ping_returns_ok(test_client):
    response = test_client.get("/ping")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "pong" in data["message"]
    assert "success" in data["status"]