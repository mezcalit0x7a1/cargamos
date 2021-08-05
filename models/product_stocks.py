from config import db

class ProductStocksModel(db.Model):

    __tablename__ = "store_products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String)
    stock = db.Column(db.Integer)
    price: db.Column(db.Double)

    #: FK
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    
