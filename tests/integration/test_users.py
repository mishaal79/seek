import json

from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy


def test_add_user(test_client: FlaskClient):
    response = test_client.post(
        "/users",
        data=json.dumps({"username": "testuser", "password": "plaintext"}),
        content_type="application/json",
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "success" in data["message"]


def test_add_user_invalid_json(test_client: FlaskClient):
    response = test_client.post(
        "/users",
        data=json.dumps({"user": "testuser", "password": "plaintext"}),
        content_type="application/json",
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_user_duplicate_email(test_client: FlaskClient):
    response = test_client.post(
        "/users",
        data=json.dumps({"username": "testuser", "password": "plaintext"}),
        content_type="application/json",
    )
    response = test_client.post(
        "/users",
        data=json.dumps({"username": "testuser", "password": "plaintext"}),
        content_type="application/json",
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert "User already exists" in data["message"]


def test_get_user_by_id(test_client: FlaskClient, add_user):
    user = add_user("test", "plaintext")
    response = test_client.get(f"/users/{user.id}")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "test" in data["username"]


def test_get_all_users(test_client: FlaskClient, add_user):
    users = [
        add_user("test", "plaintext"),
        add_user("user", "plaintext"),
        add_user("user 2", "plaintext"),
    ]
    response = test_client.get("/users")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data) == len(users)
