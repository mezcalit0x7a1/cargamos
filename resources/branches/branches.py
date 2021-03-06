from config import api, db
from flask_restx import Resource, abort
from models.branches import BranchesModel
from schemas.branches import branches_fields , branches_parser


class Branches(Resource):
    @api.marshal_with(branches_fields, envelope='resource')
    def get(self):
        """Get all branches

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        branch = db.session.query(BranchesModel).all()
        return branch, 200

    @api.marshal_with(branches_fields, envelope='resource')
    def post(self):
        """Create branch

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        data = branches_parser.parse_args(strict=True)
        branch = BranchesModel(**data)
        try:
            db.session.add(branch)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
        return branch, 201


class Branch(Resource):
    @api.marshal_with(branches_fields, envelope='resource')
    def get(self, id):
        """Get branch from DB

        Args:
            id (int): Branch id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        branch = BranchesModel.query.get(id)
        if branch:
            return branch, 200
        abort(404, message="Branch does not exist")

    def put(self, id):
        """Update branch from DB

        Args:
            id (int): Branch id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        data = branches_parser.parse_args(strict=True)
        branch = BranchesModel.query.get(id)
        if branch:
            branch.name = data['name']
            try:
                db.session.add(branch)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 204
        abort(404, message="Branch does not exist")

    def delete(self, id):
        """Delete branch from DB

        Args:
            id (int): Branch id

        Returns:
            restx.Response: standard HTTP JSON response.
        """
        branch = BranchesModel.query.get(id)
        if branch:
            try:
                db.session.delete(branch)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                abort(500, message=str(e))
            return {}, 200
        abort(404, message="Store does not exist")
