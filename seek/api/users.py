from flask import Blueprint, request
from flask.globals import current_app
from flask.helpers import make_response
from flask_restx import Api, Resource, fields

from seek import db
from seek.api.models import User

users_blueprint = Blueprint("users", __name__)

api = Api(users_blueprint)

user = api.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)


@api.route("/users")
class Users(Resource):
    @api.expect(user, validate=True)
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        response = {}

        current_app.logger.info("Checking whether user already exists")
        if User.query.filter_by(username=username).first():
            response["message"] = "User already exists"
            return response, 400
        user = User(username, password)
        try:
            current_app.logger.info("Creating user on database")
            db.session.add(user)
            current_app.logger.info("user added to database")
            db.session.commit()
        except Exception as e:
            response["message"] = f"Failed to add user to database: {e.args}"
            return response, 500
        response["message"] = "success"
        return response, 201
