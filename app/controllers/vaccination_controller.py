from flask import request, jsonify
from app.models.vaccination_model import Vaccination
from datetime import datetime, timedelta
from app.configs.database import db


def create_vaccine_card():
    data = request.get_json()

    if not data['cpf'].isdigit() or len(data['cpf']) > 11:
        return {'msg': 'The CPF field must contain a maximum of 11 characters and only numbers'}, 400

    data['first_shot_date'] = datetime.today()

    first_shot = data['first_shot_date']
    data['second_shot_date'] = first_shot + timedelta(days = 90)

    vaccine = Vaccination(**data)

    db.session.add(vaccine)
    db.session.commit()

    return jsonify(vaccine), 201


def get_all_vaccines_cards():
    vaccines_list = Vaccination.query.all()
    return jsonify(vaccines_list), 200