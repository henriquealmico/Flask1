from app.model import BaseModel
from app.extensions import db

from flask import Blueprint
dono_api = Blueprint("dono_api", __name__)

class DonosEGatos(BaseModel):
    __tablename__ = "donos_gatos"

    id = db.Column(db.Integer, primary_key=True)
    dono = db.Column(db.Integer, db.ForeignKey("dono.id"))
    gato = db.Column(db.Integer, db.ForeignKey("gato.id"))

class Dono(BaseModel):
    __tablename__ = "dono"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))

    cao = db.relationship("Cao", backref="dono", uselist=False)
    gatos = db.relationship("Cat", secondary="donos_gatos", backref="donos")
