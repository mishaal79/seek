from flask.app import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
import pytest
from seek import create_app, db
from seek.api.models import User


@pytest.fixture
def test_app(scope="module", config="seek.config.TestingConfig") -> Flask:
    """ Returns a flask app instance initialised with test config"""
    app = create_app()
    app.config.from_object(config)
    with app.app_context():
        yield app


@pytest.fixture
def test_client(test_app, test_db, scope="function", autouse=True) -> FlaskClient:
    """ Returns a flask test client instance initialised with test config"""
    with test_app.app_context():
        yield test_app.test_client()


@pytest.fixture
def test_db(scope="function", autouse=True) -> SQLAlchemy:
    """ Returns a db instance initialised with test config"""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_user():
    """
    Returns a new test user
    """

    def _add_user(username, password):
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
