from sqlalchemy import and_, or_
from config import api, db
from flask_restx import Resource, abort
from models.store_products import StoreProductsModel
from schemas.store_products import store_products_fields, store_products_parser, store_products_stock


class StoreProduct(Resource):
    @api.marshal_with(store_products_fields, envelope="resource")
    def post(self):
        data = store_products_parser.parse_args(strict=True)
        store_id = data["store_id"]
        product_id = data["product_id"]
        sku = data["sku"]
        store_product = (
            db.session.query(StoreProductsModel)
            .filter(
                or_(
                    StoreProductsModel.sku == sku,
                    and_(StoreProductsModel.store_id == store_id, StoreProductsModel.product_id == product_id),
                )
            )
            .first()
        )
        if store_product:
            if store_product.sku == sku:
                abort(400, message=f"SKU {sku} already exists")
            else:
                abort(400, message=f"Store {store_id} already has the product {product_id}")
        store_product = StoreProductsModel(**data)
        try:
            db.session.add(store_product)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
        return store_product, 201


class StoreProducts(Resource):
    @api.marshal_with(store_products_fields, envelope="resource")
    def get(self, id):
        store_product = db.session.query(StoreProductsModel).filter(StoreProductsModel.store_id == id).all()
        return store_product, 200


class StoreProd(Resource):
    @api.marshal_with(store_products_fields, envelope="resource")
    def patch(self, id):
        data = store_products_stock.parse_args(strict=True)
        store_product = StoreProductsModel.query.get(id)
        quantity = data["quantity"]
        if quantity > 0 and store_product:
            if store_product.stock >= quantity:
                store_product.stock = store_product.stock - quantity
                try:
                    db.session.add(store_product)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    abort(500, message=str(e))
                return store_product, 200
            else:
                abort(400, message="Out of stock")
        else:
            abort(400, message="Invalid quantity")

    def put(self, id):
        data = store_products_parser.parse_args(strict=True)
        store_product = StoreProductsModel.query.get(id)
        if store_product:
            store_product.sku = data["sku"]
            store_product.stock = data["stock"]
            store_product.price = data["price"]
            store_product.product_id = data["product_id"]
            store_product.store_id = data["store_id"]
            try:
                db.session.add(store_product)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 204
        abort(404, message="Store product does not exist")
