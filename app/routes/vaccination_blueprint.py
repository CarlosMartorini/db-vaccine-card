from flask import Blueprint
from app.controllers.vaccination_controller import

bp = Blueprint('vaccination_bp', __name__, url_prefix='/vaccination')

