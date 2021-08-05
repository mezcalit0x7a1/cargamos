# -*- coding: utf-8 -*-
"""
    models.stores
    ~~~~~~~~~~~~~~
    Store ORM model
    :copyright: (c) 2021 by Luis Rdz
"""
from config import db


class StoresModel(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(10))
    phone = db.Column(db.String(10))
    email = db.Column(db.String(200))
