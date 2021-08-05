# -*- coding: utf-8 -*-
"""
    resources.store_products
    ~~~~~~~~~~~~~~
    Store products routes
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from .store_products import StoreProducts, StoreProduct, StoreProd

#: Endpoints
api.add_resource(StoreProduct, "/store_products")
api.add_resource(StoreProducts, "/store_products/stores/<int:id>")
api.add_resource(StoreProd, "/store_products/<int:id>")
