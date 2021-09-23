from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Vaccination(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vacine_name: str
    health_unit_name: str

    __tablename__ = 'vaccine_card'

    cpf = db.Column(db.String(11), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    first_shot_date = db.Column(db.DateTime())
    second_shot_date = db.Column(db.DateTime())
    vacine_name = db.Column(db.String(255), nullable=False)
    health_unit_name = db.Column(db.String(255))

