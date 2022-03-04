from flask_marshmallow import Schema
#from marshmallow.fields import Str

class ProductSchema(Schema):
    class Meta:
        fields = ["id", "category_id", "name", "description"]

