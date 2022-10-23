from enum import unique
import os
from unicodedata import category
from sqlalchemy import Column, ForeignKey, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

# Define database
database_name = 'miniecommerce'
database_path = 'postgresql://{}:{}@{}/{}'.format('mike-savy','dreamlife!','localhost:5432',database_name)

db = SQLAlchemy()


# setup(app) binds flask app to SQLAlchemy service

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PYTHONUNBUFFERED"]= ""
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()


# Categories
class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category = Column(String)


    def __init__(self, category):
      self.category = category



class Product(db.Model):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key = True)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    sku = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    measure = Column(String, nullable=False)


    def __init__(self, price, category_id, sku, name, measure ):
        self.name = name
        self.sku = sku
        self.price = price
        self.category_id = category_id
        self.measure = measure

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return  {
          'id': self.id,
          'name': self.name,
          'sku': self.sku,
          'category_id' : self.category_id,
          'measure': self.measure  
        }