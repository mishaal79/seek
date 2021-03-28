import os

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()


def create_app():
    """ "
    Flask application factory
    Return: instance of flask app
    """
    app = Flask(__name__)

    app.config.from_object(os.getenv("APP_SETTINGS"))
    api.init_app(app, "Seek API")
    db.init_app(app)

    # register blueprints
    from seek.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
