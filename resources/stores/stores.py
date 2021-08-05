# -*- coding: utf-8 -*-
"""
    resources.stores.stores
    ~~~~~~~~~~~~~~
    Store CRUD Resources
    :copyright: (c) 2021 by Luis Rdz
"""
from config import api, db
from flask_restx import Resource, abort
from models.stores import StoresModel
from schemas.stores import stores_fields, stores_parser


class Stores(Resource):
    @api.marshal_with(stores_fields, envelope="resource")
    def get(self):
        """Get all stores

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        stores = db.session.query(StoresModel).all()
        return stores, 200

    @api.marshal_with(stores_fields, envelope="resource")
    def post(self):
        """Create store

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        data = stores_parser.parse_args(strict=True)
        store = StoresModel(**data)
        try:
            db.session.add(store)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
        return store, 201


class Store(Resource):
    @api.marshal_with(stores_fields, envelope="resource")
    def get(self, id):
        """Get store from DB

        Args:
            id (int): Store id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        store = StoresModel.query.get(id)
        if store:
            return store, 200
        abort(404, message="Store does not exist")

    def put(self, id):
        """Update store from DB

        Args:
            id (int): Store id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        data = stores_parser.parse_args(strict=True)
        store = StoresModel.query.get(id)
        if store:
            store.name = data["name"]
            store.address = data["address"]
            store.city = data["city"]
            store.state = data["state"]
            store.zip_code = data["zip_code"]
            store.phone = data["phone"]
            store.email = data["email"]
            try:
                db.session.add(store)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 204
        abort(404, message="Store does not exist")

    def delete(self, id):
        """Delete store from DB

        Args:
            id (int): Store id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        store = StoresModel.query.get(id)
        if store:
            try:
                db.session.delete(store)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 200
        abort(404, message="Store does not exist")
