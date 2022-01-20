# wsgi.py
# pylint: disable=missing-docstring
BASE_URL = '/api/v1'

from flask_migrate import Migrate
from flask import Flask, request
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  # NEW LINE (L'ordre est important ici !)
db = SQLAlchemy(app)
ma = Marshmallow(app)  # NEW LINE


from models import Product
from schemas import many_product_schema
from schemas import one_product_schema
migrate = Migrate(app, db)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/product/<id>', methods=['GET'])
def get_one_product(id):
    product = db.session.query(Product).get(id)
    return one_product_schema.jsonify(product), 200