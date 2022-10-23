from crypt import methods
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import os


from database.models import setup_db, Category, Product



def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Initializa Cors
    CORS(app, resources={r"*": {"origins": "*"}})


    #   After Request
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization,true")  
        response.headers.add("Access-Control-Allow-Methods", "POST,GET,PUT,DELETE,OPTIONS")
        return response

    @app.route('/produts', methods=["POST"])
    def products():
        body = request.get_json()
        new_sku = body.get('sku', None)
        new_name = body.get('name', None)
        new_price = body.get('price', None)
        new_category_id = body.get('category_id', None)
        new_measure = body.get('measure',None)

        if ( Product.query.filter(Product.sku == new_sku)):
            abort(409)

        add_product = Product(
          sku = new_sku,
          name = new_name,
          price = new_price,
          category_id = new_category_id,
          measure = new_measure
        )

        add_product.insert()

        return jsonify ({
          'success': True
        })
      

    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
          "success":False,
          "error": 409,
          "message": "sku conflict"
        }), 409

    return app