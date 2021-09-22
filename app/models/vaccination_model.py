from app.configs.database import db

class Vaccination(db.Model):
    __tablename__ = 'vaccine_card'

    cpf = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    first_shot_date = db.Column(db.Date())
    second_shot_date = db.Column(db.Date())
    vacine_name = db.Column(db.String(255), nullable=False)
    health_unit_name = db.Column(db.String(255))