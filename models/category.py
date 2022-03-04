from database.database import db

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    parent_id = db.Column(db.Integer)


    def __init__(self, name, description, parent_id) -> None:
        self.name = name
        self.description = description
        self.parent_id = parent_id

    def json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'parent_id': str(self.parent_id)
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