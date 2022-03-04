from flask_restful import Resource, reqparse
from models.category import CategoryModel
from flasgger import swag_from


class Category(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            required=False,
            help='Название')
        self.parser.add_argument('description',
            required=False,
            help='Описание')
        self.parser.add_argument('parent_id',
            required=False,
            help='Категория родителя')

    @swag_from(methods=['GET'])
    def get(self, category_id):
        category = CategoryModel.find_by_id(category_id)

        if category:
            return category.json()
        return {'message': 'Категория с таким номером не найдена'}, 404

    @swag_from(methods=['PUT'])
    def put(self, category_id):
        category = CategoryModel.find_by_id(category_id)

        if category:
            data = self.parser.parse_args()
            category.name = data['name']
            category.description = data['description']
            category.parent_id = data['parent_id']
            category.save_to_db()
            return category.json()

        return {'message': 'Такой категории нет'}, 404

    @swag_from(methods=['DELETE'])
    def delete(self, category_id):
        category = CategoryModel.find_by_id(category_id)

        if category:
            category.delete_from_db()
        return {'message': 'Категория удалена'}