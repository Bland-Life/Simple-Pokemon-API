from pokeapp import db

class Pokemon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=True, nullable=False)
        species = db.Column(db.String)
        types = db.Column(db.String)
        height = db.Column(db.String)
        weight = db.Column(db.String)
        abilities = db.Column(db.String)
        evolutions = db.Column(db.String)
        facts = db.Column(db.String)
        site_link = db.Column(db.String)
        img_link = db.Column(db.String)
