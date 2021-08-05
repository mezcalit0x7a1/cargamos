# -*- coding: utf-8 -*-
"""
    schemas.categories
    ~~~~~~~~~~~~~~
    Response marshalling and request parsing for categories
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from flask_restx import fields, reqparse

#: Response marshalling
categories_fields = api.model("CategoriesModel", {"id": fields.Integer, "name": fields.String})

#: Request parsing
categories_parser = reqparse.RequestParser()
categories_parser.add_argument("name", required=True, location="json")
