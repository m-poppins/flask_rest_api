from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger

from database.database import db

from controller.productController import Product
from controller.productListController import ProductList
from controller.categoryController import Category
from controller.categoryListController import CategoryList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title': 'API',
    'uiversion': 3
}
swagger = Swagger(app, template_file='swagger.yml')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

'''@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response '''

api.add_resource(Product, '/api/products/<int:product_id>')
api.add_resource(ProductList, '/api/products')
api.add_resource(Category, '/api/categories/<int:category_id>')
api.add_resource(CategoryList, '/api/categories')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)