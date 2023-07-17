from flask import jsonify, request
from flask_restful import Resource
from pokeapp import db
from db_model import Pokemon

AUTHENTICATION_KEY = "12345"


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
    def post(self, pokemon_name):
        auth_key = request.args.get("authkey")
        id = request.args.get("id")
        species = request.args.get("species")
        types = request.args.get("types")
        height = request.args.get("height")
        weight = request.args.get("weight")
        abilities = request.args.get("abilities")
        evolutions = request.args.get("evolutions")
        facts = request.args.get("facts")
        site_link = request.args.get("site_link")
        img_link = request.args.get("img_link")

        if not auth_key or auth_key != AUTHENTICATION_KEY:
            return 'Not Authorized To Post New Pokemon', 403
        
        if not pokemon_name:
            return 'Must include the Pokemon name in the url path!', 400


        if all(value is not None for value in (species, types, height, weight, abilities, evolutions, facts, site_link, img_link)):
            if id:
                new_pokemon = Pokemon(
                    id = id,
                    name = pokemon_name,
                    species = species,
                    types = types,
                    height = height,
                    weight = weight,
                    abilities = abilities,
                    evolutions = evolutions,
                    facts = facts,
                    site_link = site_link,
                    img_link = img_link
                )
                db.session.add(new_pokemon)
                db.session.commit()
                return jsonify(pokemon=Pokemon.query.filter_by(name=pokemon_name).first())
            else: 
                new_pokemon = Pokemon(
                    name = pokemon_name,
                    species = species,
                    types = types,
                    height = height,
                    weight = weight,
                    abilities = abilities,
                    evolutions = evolutions,
                    facts = facts,
                    site_link = site_link,
                    img_link = img_link
                )
                db.session.add(new_pokemon)
                db.session.commit()
                return jsonify(pokemon=Pokemon.query.filter_by(name=pokemon_name).first())
        else:
            return 'Missing required parameters!', 400
        
    def delete(self, pokemon_to_del):
        if not pokemon_to_del:
            return 'Must include the Pokemon name in the url path!', 400
        
        current_pokemon = Pokemon.query.filter_by(name=pokemon_to_del).first()
        auth_key = request.args.get('authkey')
        if not current_pokemon:
            return 'No Pokemon with this name was discovered in the database!', 400
        if not auth_key or auth_key != AUTHENTICATION_KEY:
            return 'Not Authorized To Delete Pokemon!', 403
        
        db.session.delete(current_pokemon)
        db.session.commit()
        return jsonify(pokemon=current_pokemon)

        
class PokemonID(Resource):
    def get(self, national_id):
        if not national_id:
            return "No ID was given.", 400

        pokemon = Pokemon.query.get(national_id)
        if pokemon:
            return jsonify(pokemon=pokemon)
        else:
            return "Invalid Nationaldex ID" 