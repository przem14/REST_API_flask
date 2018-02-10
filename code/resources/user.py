from functools import wraps
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "The username must be provided."
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "The password must be provided."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User {} arleady exists.".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201