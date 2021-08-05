from config import api
from flask_restx import fields, reqparse

categories_fields = api.model('CategoriesModel', {
    'id': fields.Integer,
    'name': fields.String
})

categories_parser = reqparse.RequestParser()
categories_parser.add_argument('name', required=True, location='json')
