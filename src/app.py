from crypt import methods
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import os

from numpy import empty


from database.models import setup_db, Category, Product



def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Initializa Cors
    CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})
   
    #   After Request
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization,true")  
        response.headers.add("Access-Control-Allow-Methods", "POST,GET,PUT,DELETE,OPTIONS")
        return response

# Post Product
    @app.route('/products', methods=["POST"])
    def products():
        body = request.get_json()
        new_sku = body.get('sku', None)
        new_name = body.get('name', None)
        new_price = body.get('price', None)
        new_category_id = body.get('category_id', None)
        new_measure = body.get('measure',None)
       
        if( new_sku == None or 
          new_name == None or 
          new_price == None or 
          new_category_id == None or 
          new_measure == None 
        ):
          abort(404)

        product_all = Product.query.all()

        for product in product_all:
            if(product.sku == new_sku):
                abort(409)
        
        add_product = Product(
          sku = new_sku,
          name = new_name,
          price = new_price,
          category_id = new_category_id,
          measure = new_measure
        )

        add_product.insert()

        products = Product.query.all()
        products_formated = [ product.format() for product in products]

        return jsonify ({
          'success': True,
          'products': products_formated,
          'product_length': len(products) 
        })

# Get product
    @app.route('/products', methods=["GET"])
    def get_products():
        products = Product.query.all()

        products_formated = [ product.format() for product in products]

        return jsonify({
          'success': True,
          'products': products_formated,
          'product_length': len(products) 
        })

# Delete Products
    @app.route('/products', methods=['DELETE'])
    def delete_product():
        body = request.get_json()
        print('Here is delete list',body)
        delete_list = body.get('list', None)
        if (len(delete_list) == 0):
            abort(404)

        for id in delete_list:
            product = Product.query.get(id)
            if(product is not None):
              product.delete()
            else: 
              abort(404)


        product_left = Product.query.all()
        products = [product.format() for product in product_left]

        return jsonify({
          "success":True,
          "product": products,
          "product_length": len(product_left)
        })

      

    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
          "success":False,
          "error": 409,
          "message": "sku conflict"
        }), 409

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          "success":False,
          "error": 404,
          "message": "Not Found"
        })

    return app