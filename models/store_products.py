# -*- coding: utf-8 -*-
"""
    models.store_products
    ~~~~~~~~~~~~~~
    Store Products ORM model
    :copyright: (c) 2021 by Luis Rdz
"""
from config import db


class StoreProductsModel(db.Model):

    __tablename__ = "store_products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(32))
    stock = db.Column(db.Integer)
    price = db.Column(db.Numeric)

    #: FK
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
