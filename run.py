# -*- coding: utf-8 -*-

from database import db_session, init_db
from atendimentos.models import *
from colaboradores.models import *
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, marshal, marshal_with
from flask.ext.httpauth import HTTPBasicAuth
from sqlalchemy import func
from configuracao import *
import json

 
app = Flask(__name__, static_url_path = "")
app.secret_key = chave
api = Api(app)
auth = HTTPBasicAuth()
 
@auth.get_password
def get_password(username):
    colaborador = Colaborador.query.filter(func.lower(Colaborador.nome)==func.lower(username), Colaborador.ativo=='SIM').first()

    if colaborador:
        return colaborador.senha
    else:
        return None
 
@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'message': 'Nao autorizado!' } ), 403)


class atendimentos_api(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(atendimentos_api, self).__init__()
        
    @marshal_with(atendimento_campos)
    def get(self):
        atendimentos = Atendimento.query.filter(Atendimento.ativo=='SIM')
        return atendimentos.all()

    @marshal_with(atendimento_campos)
    def post(self):
        args = self.reqparse.parse_args()
        atendimento = Atendimento()

        atendimento.empresa = args['empresa']
        atendimento.pessoa = args['pessoa']
        atendimento.email = args['email']
        atendimento.relato = args['relato']
        atendimento.data_cadastro = args['data_cadastro']
        atendimento.data_atendimento = args['data_atendimento']
        atendimento.observacao = args['observacao']
        atendimento.categoria = args['categoria']
        atendimento.satisfacao = args['satisfacao']
        atendimento.satisfacao_observacao = args['satisfacao_observacao']
        atendimento.retornar = args['retornar']
        atendimento.ativo = args['ativo']

        atendimento.post()
        return atendimento


api.add_resource(atendimentos_api, '/atendimentos')
    
if __name__ == '__main__':
    init_db()
    app.run(debug = True)