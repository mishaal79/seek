import os

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_blueprints(app):
    raise NotImplementedError


def create_app():
    """ "
    Flask application factory
    Return: instance of flask app
    """
    app = Flask(__name__)

    app.config.from_object(os.getenv("APP_SETTINGS"))
    db.init_app(app)

    # register blueprints
    from seek.api.ping import ping_blueprint
    from seek.api.users import users_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(ping_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
