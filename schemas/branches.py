from config import api
from flask_restx import fields, reqparse

branches_fields = api.model('BranchesModel', {
    'id': fields.Integer,
    'name': fields.String
})

branches_parser = reqparse.RequestParser()
branches_parser.add_argument('name', required=True, location='json')
