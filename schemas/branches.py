# -*- coding: utf-8 -*-
"""
    schemas.branches
    ~~~~~~~~~~~~~~
    Response marshalling and request parsing for branches
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api
from flask_restx import fields, reqparse

#: Response marshalling
branches_fields = api.model("BranchesModel", {"id": fields.Integer, "name": fields.String})

#: Request parsing
branches_parser = reqparse.RequestParser()
branches_parser.add_argument("name", required=True, location="json")
