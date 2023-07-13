from flask import jsonify, request
from flask_restful import Resource
from pokeapp import db
from db_model import Pokemon

class Hello(Resource):
    def get(self):
        return "Welcome to the Simple Pokemon API!"
    
class Pokedex(Resource):
    def get(self):
        count = request.args.get("count")
        if count and count.isdigit():
            if int(count) > Pokemon.query.count():
                return "Count is outside of current Pokedex range.", 400
            return jsonify(pokemons=Pokemon.query.all()[:int(count)])
        elif count and not count.isdigit():
            return "Count must be a positive integer.", 400
        return jsonify(pokemons=Pokemon.query.all())
    
class PokemonName(Resource):
    def get(self):
        poke_name = request.args.get("name")
        if poke_name:
            poke_name = poke_name.title()
            return jsonify(pokemon=Pokemon.query.filter_by(name=poke_name).first())
        else:
            return 'The "name" parameter is required and, currently, missing.', 400
        
class PokemonID(Resource):
    def get(self, national_id):
        if not national_id:
            return "No ID was given.", 400

        pokemon = Pokemon.query.get(national_id)
        if pokemon:
            return jsonify(pokemon=pokemon)
        else:
            return "Invalid Nationaldex ID" 
        