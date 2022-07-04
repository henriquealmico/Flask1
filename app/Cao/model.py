from app.model import BaseModel
from app.extensions import db

from flask import Blueprint
cao_api = Blueprint("cao_api", __name__)

class Cao(BaseModel):
    __tablename__ = "cao"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    raca = db.Column(db.String(20))

    dono = db.Column(db.Integer, db.ForeignKey("dono.id"))
