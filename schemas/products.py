from config import api
from flask_restx import fields, reqparse
from .branches import branches_fields
from .categories import categories_fields

products_fields = api.model('ProductsModel', {
    'id': fields.Integer,
    'name': fields.String,
    'id_category': fields.Integer,
    'id_branch': fields.Integer,
})

products_full_fields = api.model('ProductsModel', {
    'id': fields.Integer,
    'name': fields.String,
    'branch': fields.Nested(branches_fields),
    'category': fields.Nested(categories_fields),
})

products_parser = reqparse.RequestParser()
products_parser.add_argument('name', required=True, location='json')
products_parser.add_argument('id_category', type=int, required=True,location='json')
products_parser.add_argument('id_branch', type=int, required=True, location='json')
