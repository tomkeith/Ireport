from flask import Blueprint
from flask_restful import Api, Resource

from .redflags.views import RedFlags, RedFlag
from .users.views import Users


api_version_one = Blueprint('apiv1', __name__, url_prefix="/api/v1")
api = Api(api_version_one)

api.add_resource(RedFlags, "/redflags")
api.add_resource(Users, "/users")
api.add_resource(RedFlag, "/redflag/<int:num>")