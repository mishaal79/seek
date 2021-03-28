from flask_sqlalchemy import SQLAlchemy
import pytest
from seek import create_app, db


@pytest.fixture
def test_app(scope="module"):
    """ Returns an app instance initialised with test config"""
    app = create_app()
    app.config.from_object("seek.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture
def test_db(scope="module"):
    """ Returns a db instance initialised with test config"""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
