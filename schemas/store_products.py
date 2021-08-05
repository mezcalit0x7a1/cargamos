# -*- coding: utf-8 -*-
"""
    schemas.store_products
    ~~~~~~~~~~~~~~
    Response marshalling and request parsing for store products
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from flask_restx import fields, reqparse

#: Response marshalling
store_products_fields = api.model(
    "StoreProductsModel",
    {
        "id": fields.Integer,
        "sku": fields.String,
        "stock": fields.Integer,
        "price": fields.Float,
        "product_id": fields.Integer,
        "store_id": fields.Integer,
    },
)

#: Request parsing
store_products_parser = reqparse.RequestParser()
store_products_parser.add_argument("sku", required=True, location="json")
store_products_parser.add_argument("stock", type=int, required=True, location="json")
store_products_parser.add_argument("price", type=float, required=True, location="json")
store_products_parser.add_argument("product_id", type=int, required=True, location="json")
store_products_parser.add_argument("store_id", type=int, required=True, location="json")

store_products_stock = reqparse.RequestParser()
store_products_stock.add_argument("quantity", type=int, required=True, location="json")
