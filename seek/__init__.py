import os

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

# api.init_app(app)
api = Api(app)
db.init_app(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# @api.route("/hello")
class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "pong pong",
        }


api.add_resource(Ping)
