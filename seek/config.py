import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("APP_KEY", "secret")


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_TEST_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_TEST_URL")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")