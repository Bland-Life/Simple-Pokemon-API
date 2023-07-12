from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import csv

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
     api.add_resource(Pokedex, "/search")

     api.init_app(app)


def db_from_csv(app: Flask, csv_path):
    with open(csv_path, mode='r', encoding='UTF8') as file:
        pokemons = csv.reader(file)
        
        # Necessary to add and commit to the database
        with app.app_context():

            for pokemon in pokemons:
                
                # The first row is the headers, this helps skip over the headers
                if pokemon[0] == "id":
                    continue

                new_pokemon = Pokemon(
                    id = int(pokemon[0]),
                    name= pokemon[1],
                    species = pokemon[2],
                    types = pokemon[3].strip('[]'),
                    height = pokemon[4],
                    weight = pokemon[5],
                    abilities = pokemon[6].strip('[]'),
                    evolutions = pokemon[7].strip('[]'),
                    facts = pokemon[8],
                    site_link = pokemon[9],
                    img_link = pokemon[10]
                )

                db.session.add(new_pokemon)
                db.session.commit()
    