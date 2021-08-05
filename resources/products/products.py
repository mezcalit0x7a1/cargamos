from config import api, db
from flask_restx import Resource, abort
from models.products import ProductsModel
from schemas.products import products_fields, products_parser, products_full_fields


class Products(Resource):
    @api.marshal_with(products_full_fields, envelope='resource')
    def get(self):
        product = db.session.query(ProductsModel).all()
        return product, 200

    @api.marshal_with(products_fields, envelope='resource')
    def post(self):
        data = products_parser.parse_args(strict=True)
        product = ProductsModel(**data)
        try:
            db.session.add(product)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
        return product, 201


class Product(Resource):
    @api.marshal_with(products_full_fields, envelope='resource')
    def get(self, id):
        product = ProductsModel.query.get(id)
        if product:
            return product, 200
        abort(404, message="Product does not exist")

    def put(self, id):
        data = products_parser.parse_args(strict=True)
        product = ProductsModel.query.get(id)
        if product:
            product.name = data['name']
            product.id_category = data['id_category']
            product.id_branch = data['id_branch']
            try:
                db.session.add(product)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 204
        abort(404, message="Product does not exist")

    def delete(self, id):
        product = ProductsModel.query.get(id)
        if product:
            try:
                db.session.delete(product)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 200
        abort(404, message="Product does not exist")
