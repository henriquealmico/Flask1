from datetime import date
from app.Cao.model import Cao
from flask import request, jsonify
from flask.views import MethodView


class CaoCreate(MethodView):  #/registro

    def post(self):

        body = request.json

        id = body.get('id')
        nome = body.get('nome')
        raca = body.get('raca')
        cor = body.get('cor')
        data_nascimento = body.get('data_nascimento')
        nacionalidade = body.get('nacionalidade')
        dono = body.get('dono')

        if isinstance(nome, str) and \
            isinstance(raca, str) and \
                isinstance(cor, str) and \
                    isinstance(nacionalidade, str):
                        
            cao = Cao.query.filter_by(nome=nome).first()

            if cao:
                return {"code_status": "Dados inválidos, cao ja cadastrado"}, 400

            cao = Cao(nome=nome, 
                        raca=raca, 
                        cor=cor, 
                        data_nascimento=data_nascimento, 
                        nacionalidade=nacionalidade)

            cao.save()

            return cao.json(), 200

    
    def get(self):

        caes = Cao.query.all()

        return jsonify([cao.json() for cao in caes]), 200


class CaoDetails(MethodView):

    def get(self, id):

        cao = Cao.query.get_or_404(id)

        return cao.json()

    
    def put(self, id):

        body = request.json
        cao = Cao.query.get_or_404(id)

        nome = body.get('nome')
        raca = body.get('raca')
        cor = body.get('cor')
        data_nascimento = body.get('data_nascimento')
        nacionalidade = body.get('nacionalidade')

        if isinstance(nome, str) and \
            isinstance(raca, str) and \
                isinstance(cor, str) and \
                    isinstance(data_nascimento, date) and \
                        isinstance(nacionalidade, str):

            cao.nome = nome
            cao.raca = raca
            cao.cor = cor
            cao.data_nascimento = data_nascimento
            cao.nacionalidade = nacionalidade

            cao.update()

            return cao.json(), 200

        else: 
            return {"code_status": "dados invalidos"}, 400

    
    def patch(self,id):

        body = request.json
        cao = Cao.query.get_or_404(id)

        nome = body.get('nome', cao.nome)
        raca = body.get('raca', cao.raca)
        cor = body.get('cor', cao.cor)
        data_nascimento = body.get('data_nascimento', cao.data_nascimento)
        nacionalidade = body.get('nacionalidade', cao.nacionalidade)

        if isinstance(nome, str) and \
            isinstance(raca, str) and \
                isinstance(cor, str) and \
                    isinstance(data_nascimento, date) and \
                        isinstance(nacionalidade, str):

            cao.nome = nome
            cao.raca = raca
            cao.cor = cor
            cao.data_nascimento = data_nascimento
            cao.nacionalidade = nacionalidade

            cao.update()

            return cao.json(), 200

    
    def delete(self, id):

        cao = Cao.query.get_or_404(id)
        cao.delete(cao)

        return cao.json()





