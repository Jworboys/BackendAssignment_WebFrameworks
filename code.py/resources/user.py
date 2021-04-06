import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse


class UserRegister(Resource):

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return{"message": "A user with that username already exits."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return{"message": "User created successfully."}, 201