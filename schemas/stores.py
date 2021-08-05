# -*- coding: utf-8 -*-
"""
    schemas.stores
    ~~~~~~~~~~~~~~
    Response marshalling and request parsing for stores
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from flask_restx import fields, reqparse

#: Response marshalling
stores_fields = api.model(
    "StoreModel",
    {
        "id": fields.Integer,
        "name": fields.String,
        "address": fields.String,
        "city": fields.String,
        "state": fields.String,
        "zip_code": fields.String,
        "phone": fields.String,
        "email": fields.String,
    },
)

#: Request parsing
stores_parser = reqparse.RequestParser()
stores_parser.add_argument("name", required=True, location="json")
stores_parser.add_argument("address", required=True, location="json")
stores_parser.add_argument("city", required=True, location="json")
stores_parser.add_argument("state", required=True, location="json")
stores_parser.add_argument("zip_code", required=True, location="json")
stores_parser.add_argument("phone", required=True, location="json")
stores_parser.add_argument("email", required=True, location="json")
