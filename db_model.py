from pokeapp import db
from dataclasses import dataclass

@dataclass
class Pokemon(db.Model):
        id: int = db.Column(db.Integer, primary_key=True)
        name: str = db.Column(db.String, unique=True, nullable=False)
        species: str = db.Column(db.String)
        types: str = db.Column(db.String)
        height: str = db.Column(db.String)
        weight: str = db.Column(db.String)
        abilities: str = db.Column(db.String)
        evolutions: str = db.Column(db.String)
        facts: str = db.Column(db.String)
        site_link: str = db.Column(db.String)
        img_link: str = db.Column(db.String)
