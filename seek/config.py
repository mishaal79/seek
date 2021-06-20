import os


class Base:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("APP_KEY", "secret")


class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")


class Testing(Base):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")


class Production(Base):
    database_url = os.environ.get("DATABASE_URL")

    if database_url is not None and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url
