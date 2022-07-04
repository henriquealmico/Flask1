from app.Cao.controller import CaoCreate, CaoDetails
from flask import Blueprint

cao_api = Blueprint("cao_api", __name__)

cao_api.add_url_rule('/registro', view_func=CaoCreate.as_view("registro"), methods = ['POST', 'GET'])
cao_api.add_url_rule('/modificar', view_func=CaoDetails.as_view("modifica_cao"), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])