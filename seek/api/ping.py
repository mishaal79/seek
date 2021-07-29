from flask import Blueprint
from flask_restx import Api, Resource

ping_blueprint = Blueprint("ping", __name__)

api = Api(ping_blueprint)


@api.route("/ping")
class Ping(Resource):
    """
    Call with GET request
    Return: pong
    """

    def get(self):
        return {
            "status": "success",
            "message": "pong pong",
        }


@api.route("/")
class Home(Resource):
    def get(self):
        return {
            "message": "welcome to my practice API"
        }
