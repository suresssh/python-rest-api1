import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = 'Items'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    
    def json(self):
        return {"name":self.name,"price":self.price}

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @classmethod
    def get_item(cls,name):
        return cls.query.filter_by(name = name).first()
    
    @classmethod
    def get_items(cls):
        return cls.query.all()
    
    def insert_item(self):
        item = ItemModel.get_item(self.name)
        if item is not None:
            return {"message":"Item already exists"},404
        db.session.add(self)
        db.session.commit()
        return {"message":"Item inserted"}
    
    def update_or_insert_item(self):
        item = ItemModel.get_item(self.name)
        if item is None: 
            db.session.add(self)
            db.session.commit()
        else:
            item.price = self.price
            db.session.add(item)
            db.session.commit()
        return {"message" : f"Item {self.name} upserted"},200
    
    @classmethod
    def delete_item(cls,name):
        item = cls.get_item(name)
        db.session.delete(item)
        db.session.commit()
        return {"message" : f"Item {name} deleted"}
