# -*- coding: utf-8 -*-
"""
    config.api
    ~~~~~~~~~~~~~~
    Instance API Restx
    :copyright: (c) 2021 by Luis Rdz
"""
from .flask import app
from flask_restx import Api

api = Api(app)
