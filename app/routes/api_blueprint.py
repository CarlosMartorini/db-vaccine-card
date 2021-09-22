from flask import Blueprint
from . import vaccination_blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(vaccination_blueprint.bp)