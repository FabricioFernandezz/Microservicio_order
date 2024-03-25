from flask import Flask
from flask_cors import CORS
from app.config.database import db

def create_app():
    app=Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    return app