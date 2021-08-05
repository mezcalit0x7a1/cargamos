from config import db

class ProductsModel(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #: FK
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    id_branch = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)

    branch = db.relationship('BranchesModel', back_populates='products')
    category = db.relationship('CategoriesModel', back_populates='products')