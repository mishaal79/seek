import os


class Base:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("APP_KEY", "secret")


class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_TEST_URL")


class Testing(Base):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_TEST_URL")


class Production(Base):
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL")