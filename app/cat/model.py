from app.model import BaseModel
from app.extensions import db

from flask import Blueprint
gato_api = Blueprint("gato_api", __name__)

class Cat(BaseModel):
    __tablename__ = "gato"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    breed = db.Column(db.String(15))