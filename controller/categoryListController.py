from flask_restful import Resource, reqparse
from models.category import CategoryModel

from flasgger import swag_from

class CategoryList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            required=True,
            help='Название')
        self.parser.add_argument('description',
            required=True,
            help='Описание')
        self.parser.add_argument('parent_id',
            required=True,
            help='Мдентификатор категории')


    @swag_from(methods=['GET'])
    def get(self):
        return [category.json() for category in CategoryModel.query.all()]


    @swag_from(methods=['POST'])
    def post(self):
        data = self.parser.parse_args()
        category = CategoryModel(**data)

        try:
            category.save_to_db()
        except Exception as exception:
            print(exception)
            return {'message':'Не судьба'}, 500

        return category.json(), 201

    '''    @swag_from(methods=['GET'])
        def get(self):
            data = self.parser.parse_args()
            name = data.get("name")
            description = data.get("description")
            category_id = data.get("category_id")
            query = []
            if name:
                query.append(ProductModel.name == name)
            if description:
                query.append(ProductModel.description == description)
            if category_id:
                query.append(ProductModel.category_id == category_id)

            return (product.json() for product in ProductModel.query.filter(*query).all())
            #return [product.json() for product in ProductModel.query.all().filter(ProductModel.name == data.get('name'))] '''