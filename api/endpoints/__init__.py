from flask_restplus import Api
from flask import Blueprint
from .user import USER_API

API_BLUEPRINT = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(API_BLUEPRINT, default="Siemens API", version='1.0', title='Config API',
          description='API to manage Catalogs')
API.add_namespace(USER_API)


