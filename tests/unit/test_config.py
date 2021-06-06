import os


def test_development_config(test_app):
    test_app.config.from_object("seek.config.Development")
    assert test_app.config["SECRET_KEY"] == "secret"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DB_TEST_URL")


def test_testing_config(test_app):
    test_app.config.from_object("seek.config.Testing")
    assert test_app.config["SECRET_KEY"] == "secret"
    assert test_app.config["TESTING"]
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DB_TEST_URL")


def test_production_config(test_app):
    test_app.config.from_object("seek.config.Production")
    assert test_app.config["SECRET_KEY"] == "secret"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DB_URL")
