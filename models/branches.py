# -*- coding: utf-8 -*-
"""
    models.branches
    ~~~~~~~~~~~~~~
    Branches ORM model
    :copyright: (c) 2021 by Luis Rdz
"""
from config import db


class BranchesModel(db.Model):

    __tablename__ = "branches"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #: FK
    products = db.relationship("ProductsModel", back_populates="branch")
