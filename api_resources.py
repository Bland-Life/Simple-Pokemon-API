from flask import jsonify, request
from flask_restful import Resource
from pokeapp import db
from db_model import Pokemon

class Hello(Resource):
    def get(self):
        return "Welcome to the Simple Pokemon API!"
    
class Pokedex(Resource):
    def get(self):
        return jsonify(pokemons=Pokemon.query.all())
    
class PokemonName(Resource):
    def get(self):
        poke_name = request.args.get("name")
        if poke_name:
            poke_name = poke_name.title()
            return jsonify(pokemon=Pokemon.query.filter_by(name=poke_name).first())
        
class PokemonID(Resource):
    def get(self, national_id):
        if not national_id:
            return "No ID was given."
        return jsonify(pokemon=Pokemon.query.get(national_id))