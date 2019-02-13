from flask import Flask, request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT
from resources.item import Item,ItemList
from resources.user import UserRegister

from security import authenticate,identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'    
api = Api(app)
jwt = JWT(app,authenticate,identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/signup')

if __name__ == '__main__':
    from flask_sqlalchemy import  SQLAlchemy
    db = SQLAlchemy()
    db.init_app(app)
    app.run(port=5000,debug=True)