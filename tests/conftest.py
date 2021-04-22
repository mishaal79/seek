from flask.app import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
import pytest
from seek import create_app, db


@pytest.fixture
def test_app(scope="module") -> Flask:
    """ Returns a flask app instance initialised with test config"""
    app = create_app()
    app.config.from_object("seek.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture
def test_client(scope="module") -> FlaskClient:
    """ Returns a flask test client instance initialised with test config"""
    app = create_app()
    app.config.from_object("seek.config.TestingConfig")
    with app.app_context():
        yield app.test_client()


@pytest.fixture
def test_db(scope="module") -> SQLAlchemy:
    """ Returns a db instance initialised with test config"""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
