from flask import Blueprint
from app.controllers.vaccination_controller import create_vaccine_card, get_all_vaccines_cards

bp = Blueprint('vaccination_bp', __name__, url_prefix='/vaccination')

bp.post('')(create_vaccine_card)
bp.get('')(get_all_vaccines_cards)
