# -*- coding: utf-8 -*-
"""
    resources.branches
    ~~~~~~~~~~~~~~
    Branches routes
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from .branches import Branches, Branch

#: Endpoints
api.add_resource(Branches, "/branches")
api.add_resource(Branch, "/branches/<int:id>")
