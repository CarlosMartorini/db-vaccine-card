from flask import request, jsonify
from app.models.vaccination_model import Vaccination
from datetime import datetime, timedelta
from app.configs.database import db


def create_vaccine_card():
    data = request.get_json()

    data['first_shot_date'] = datetime.today()

    first_shot = data['first_shot_date']
    data['second_shot_date'] = first_shot + timedelta(days = 90)

    vaccine = Vaccination(**data)

    print(vaccine)
    print(type(data['first_shot_date']))
    print(data['first_shot_date'])
    print(type(data['second_shot_date']))
    print(data['second_shot_date'])

    db.session.add(vaccine)
    db.session.commit()

    return jsonify(vaccine), 201


def get_all_vaccines_cards():
    print("Esta executando o get_all_vaccines_cards")
    vaccines_list = Vaccination.query.all()
    return jsonify(vaccines_list), 200