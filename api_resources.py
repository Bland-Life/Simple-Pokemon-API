from flask import jsonify
from flask_restful import Resource
from pokeapp import db
from db_model import Pokemon

class Hello(Resource):
    def get(self):
        return "hello"
    
class Pokedex(Resource):
    def get(self):
        return jsonify(pokemon=Pokemon.query.all())