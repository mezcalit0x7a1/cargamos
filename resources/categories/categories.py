from config import api, db
from flask_restx import Resource, abort
from models.categories import CategoriesModel
from schemas.categories import categories_fields , categories_parser


class Categories(Resource):
    @api.marshal_with(categories_fields, envelope='resource')
    def get(self):
        """Get all categories

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        category = db.session.query(CategoriesModel).all()
        return category, 200

    @api.marshal_with(categories_fields, envelope='resource')
    def post(self):
        """Create category

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        data = categories_parser.parse_args(strict=True)
        category = CategoriesModel(**data)
        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
        return category, 201


class Category(Resource):
    @api.marshal_with(categories_fields, envelope='resource')
    def get(self, id):
        """Get category from DB

        Args:
            id (int): Category id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        category = CategoriesModel.query.get(id)
        if category:
            return category, 200
        abort(404, message="Category does not exist")

    def put(self, id):
        data = categories_parser.parse_args(strict=True)
        category = CategoriesModel.query.get(id)
        if category:
            category.name = data['name']
            try:
                db.session.add(category)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 204
        abort(404, message="Category does not exist")

    def delete(self, id):
        """Delete category from DB

        Args:
            id (int): Category id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        category = CategoriesModel.query.get(id)
        if category:
            try:
                db.session.delete(category)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 200
        abort(404, message="Category does not exist")
