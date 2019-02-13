from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

items=[{'name':'chair','price':13.50},
      {'name':'pen','price':40.50}]

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = int,
    required = True,
    help = "This field cannot be empty!"
    )
    
    @jwt_required()
    def get(self,name):
        try:
            item = ItemModel.get_item(name)
            return item.json()
        except:
            return {"message":"error in getting item"}

    @jwt_required()
    def post(self,name):
        data = Item.parser.parse_args()
        try:
           item_insert = ItemModel(name,data['price'])
           response = item_insert.insert_item()
           return response
        except:
            return {"message":"Error in inserting in item"}

    @jwt_required()
    def delete(self, name):
        try:
            response = ItemModel.delete_item(name)
            return response
        except:
            return {"message":"error in deleting item"}
    
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        try:
            update_n_insert = ItemModel(name,data['price'])
            response = update_n_insert.update_or_insert_item()
            return response
        except:
            return {"message":"Error in updating the item"}

class ItemList(Resource):

    @jwt_required()
    def get(self):
        try:
            item = ItemModel.get_items()
            return {"items":[x.json() for x in item]}
        except:
            return {"message":"error in getting list of items"}

