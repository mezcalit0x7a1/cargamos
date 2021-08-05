# -*- coding: utf-8 -*-
"""
    resources.products
    ~~~~~~~~~~~~~~
    Products routes
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from .products import Products, Product

#: Endpoints
api.add_resource(Products, "/products")
api.add_resource(Product, "/products/<int:id>")
