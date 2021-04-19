from flask.globals import current_app
from flask.helpers import make_response
from seek.api.models import User
from flask import Blueprint, request
from flask_restx import Api, Resource
from seek import db

users_blueprint = Blueprint("users", __name__)

api = Api(users_blueprint)


class Users(Resource):
    def post(self):
        response = None
        data = request.get_json()
        user = User(data.get("username"), data.get("password"))
        try:
            current_app.logger.info("Creating user on database")
            db.session.add(user)
            current_app.logger.info("user added to database")
            db.session.commit()
        except Exception as e:
            return f"Failed to add user to database: {e.args()}", 500
        return "success", 201


api.add_resource(Users, "/users")
