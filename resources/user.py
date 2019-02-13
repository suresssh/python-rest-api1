import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = "This field cannot be empty!"
    )
    
    parser.add_argument('password',
    type = str,
    required = True,
    help = "This field cannot be empty!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        sign_up = UserModel(None,data['username'],data['password'])
        response = sign_up.insert_user()
        return response




        
