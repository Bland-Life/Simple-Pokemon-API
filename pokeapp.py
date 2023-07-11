from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()
DB_NAME = "pokemon.db"
    

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    db.init_app(app)

    return app

from db_model import Pokemon
def create_db(app: Flask):

    with app.app_context():
        db.create_all()

from api_resources import *
def create_api(app: Flask):
     api.add_resource(Hello, "/")

     api.init_app(app)