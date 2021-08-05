from config import api
from .categories import Categories, Category

#: Endpoints
api.add_resource(Categories, '/categories')
api.add_resource(Category, '/categories/<int:id>')
