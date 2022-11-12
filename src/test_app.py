import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from main import create_app
from database.models import setup_db, Category, Product


class MiniEcommerce(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'miniecommerce_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('mike-savy','dreamlife!','localhost:5432',self.database_name)
        setup_db(self.app, self.database_path)


         # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    """Executed after reach test"""   
    def tearDown(self):
        pass

    def test_post_product(self):
        res = self.client().post('/products', json={'sku':'KDFUk12','name': 'shelom Homes','measure': 90,'price': 20,'category_id': 1}) 
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
              

    def test_get_product(self):
        res = self.client().get('/products')
        self.assertEqual(res.status_code, 200)

    def test_post_delete(self):
        res= self.client().post('/product', json={'list': [4,5,6]})
        self.assertEqual(res.status_code, 200);



if __name__ == "__main__":
      unittest.main()