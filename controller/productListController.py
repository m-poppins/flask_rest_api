from flask_restful import Resource, reqparse
from models.product import ProductModel
from flasgger import swag_from

class ProductList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            required=True,
            help='Название')
        self.parser.add_argument('description',
            required=True,
            help='Описание')
        self.parser.add_argument('category_id',
            required=True,
            help='Мдентификатор категории')

#    @swag_from(methods=['GET'])
#    def get(self):
#        return [product.json() for product in ProductModel.query.all()]

    @swag_from(methods=['GET'])
    def get(self):
        return [product.json() for product in ProductModel.query.all()]
        #return [product.json() for product in ProductModel.query.all().filter(ProductModel.name == data.get('name'))]


    @swag_from(methods=['POST'])
    def post(self):
        data = self.parser.parse_args()
        product = ProductModel(**data)

        try:
            product.save_to_db()
        except Exception as exception:
            print(exception)
            return {'message' : 'An error occured inserting the item.'}, 500

        return product.json(), 201

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