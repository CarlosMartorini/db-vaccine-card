from datetime import date, timedelta
from app.configs.database import db
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class Vaccination(db.Model):
    cpf: str
    name: str
    first_shot_date: date
    second_shot_date: date
    vacine_name: str
    health_unit_name: str

    __tablename__ = 'vaccine_card'

    cpf = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    first_shot_date = db.Column(db.Date())
    second_shot_date = db.Column(db.Date(), first_shot_date + timedelta(days = 90))
    vacine_name = db.Column(db.String(255), nullable=False)
    health_unit_name = db.Column(db.String(255))


    def create_vaccine_card():
        data = request.get_json()

        vaccine = Vaccination(**data)

        db.session.add(vaccine)
        db.session.commit()

        return jsonify(vaccine), 201


    def get_all_vaccines_cards():
        vaccines_list = Vaccination.query.all()
        return jsonify(vaccines_list), 200