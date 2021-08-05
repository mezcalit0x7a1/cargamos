from config import db

class CategoriesModel(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    products = db.relationship('ProductsModel', back_populates='category')
