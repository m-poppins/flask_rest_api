from database.database import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer)


    def __init__(self, name, description, category_id) -> None:
        self.name = name
        self.description = description
        self.category_id = category_id

    def json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'category_id': str(self.category_id)
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()