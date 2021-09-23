from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    
    from app.models.vaccination_model import Vaccination

    Migrate(app, app.db)