from config import db

class BranchesModel(db.Model):

    __tablename__ = "branches"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    products = db.relationship('ProductsModel', back_populates='branch')
