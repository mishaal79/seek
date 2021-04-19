import json
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy


def test_add_user(test_client: FlaskClient, test_db: SQLAlchemy):
    resp = test_client.post(
        "/users",
        data=json.dumps({"username": "testuser", "password": "plaintext"}),
        content_type="application/json",
    )
    data = json.loads(resp.get_data(as_text=True))
    assert resp.status_code == 201
    assert "success" in data