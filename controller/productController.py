from flask_restful import Resource, reqparse
from models.product import ProductModel
from flasgger import swag_from

class Product(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            required=False,
            help='Название')
        self.parser.add_argument('description',
            required=False,
            help='Описание')
        self.parser.add_argument('category_id',
            required=False,
            help='Мдентификатор категории')

    @swag_from(methods=['GET'])
    def get(self, product_id):
        product = ProductModel.find_by_id(product_id)

        if product:
            return product.json()
        return {'message': 'Продукт не найден'}, 404

    @swag_from(methods=['PUT'])
    def put(self, product_id):
        product = ProductModel.find_by_id(product_id)

        if product:
            data = self.parser.parse_args()
            product.name = data['name']
            product.description = data['description']
            product.category_id = data['category_id']
            product.save_to_db()
            return product.json(), 200

        return {'message': 'Нет такого товара'}, 404

    @swag_from(methods=['DELETE'])
    def delete(self, product_id):
        product = ProductModel.find_by_id(product_id)

        if product:
            product.delete_from_db()
        return {'message': 'Удален товар'}, 200