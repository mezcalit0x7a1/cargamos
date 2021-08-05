from config import api
from .stores import Stores, Store

#: Endpoints
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/stores/<int:id>')
