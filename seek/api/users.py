from flask import Blueprint, request
from flask.globals import current_app
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
class UsersList(Resource):
    @api.expect(user, validate=True)
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        response = {}

        # TODO: Add a user service layer to handle creating of users logic
        current_app.logger.info("Checking whether user already exists")
        if User.query.filter_by(username=username).first():
            response["message"] = "User already exists"
            return response, 400
        user = User(username, password)
        try:
            current_app.logger.info("Creating user on database")
            db.session.add(user)
            current_app.logger.info("Added user to database")
            db.session.commit()
        except Exception as e:
            response["message"] = f"Failed to add user to database: {e.args}"
            return response, 500
        response["message"] = "success"
        return response, 201

    @api.marshal_with(user, as_list=True)
    def get(self):
        return User.query.all(), 200


@api.route("/users/<id>")
class Users(Resource):
    @api.marshal_with(user)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            api.abort(404, f"user id:{id} does not exist")
        else:
            return user, 200
