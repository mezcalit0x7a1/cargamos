# -*- coding: utf-8 -*-
"""
    resources.stores
    ~~~~~~~~~~~~~~
    Store routes
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from .stores import Stores, Store

#: Endpoints
api.add_resource(Stores, "/stores")
api.add_resource(Store, "/stores/<int:id>")
# api.add_resource(ProductsInStore, "/stores/<int:id>/products")
