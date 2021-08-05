# -*- coding: utf-8 -*-
"""
    models.categories
    ~~~~~~~~~~~~~~
    Categories ORM model
    :copyright: (c) 2021 by Luis Rdz
"""
from config import db


class CategoriesModel(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #: FK
    products = db.relationship("ProductsModel", back_populates="category")
