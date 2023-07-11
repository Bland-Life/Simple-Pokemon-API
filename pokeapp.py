from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample.db"

    db.init_app(app)
    api.init_app(app)

    return app


class Pokemon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=True, nullable=False)
        species = db.Column(db.String)


def create_db(app: Flask):

    with app.app_context():
        db.create_all()


class Hello(Resource):
    def get(self):
        return "hello"
        

def create_api(app: Flask):
    
    api.add_resource(Hello, "/")
