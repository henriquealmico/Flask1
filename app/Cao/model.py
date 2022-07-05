from app.model import BaseModel
from app.extensions import db
from flask import Blueprint

class Cao(BaseModel):

    __tablename__ = "cao"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique = True)
    raca = db.Column(db.String(20))
    cor = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    nacionalidade = db.Column(db.String(20))

    #Relationships
    dono = db.Column(db.Integer, db.ForeignKey("dono.id"))

    def json(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "raca": self.raca,
            "cor": self.cor,
            "data_nascimento": self.data_nascimento,
            "nacionalidade": self.nacionalidade,
            "dono": self.dono,
        }
