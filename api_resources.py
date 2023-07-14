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
        poke_type = request.args.get("type")
        all_pokemon = Pokemon.query.all()

        if not count:
            pass
        elif not count.isdigit():
            return "'count' parameter must be a positive integer", 400
        elif int(count) > Pokemon.query.count():
            return "'count' is outside of current Pokedex range.", 400

        if poke_type and count:
            pokemon_of_type = [pokemon for pokemon in all_pokemon if poke_type.capitalize() in pokemon.types]
            return jsonify(pokemon=pokemon_of_type[:int(count)])
        
        elif poke_type:
            pokemon_of_type = [pokemon for pokemon in all_pokemon if poke_type.capitalize() in pokemon.types]
            return jsonify(pokemon=pokemon_of_type)
        
        elif count and count.isdigit():            
            return jsonify(pokemons=all_pokemon[:int(count)])
        
        else:
            return jsonify(pokemons=all_pokemon)
    
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