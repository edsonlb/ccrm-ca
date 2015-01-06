# coding=utf-8

from database import db_session, init_db
from atendimentos.models import Atendimento
from colaboradores.models import Colaborador
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.views import MethodView
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth
from sqlalchemy import func
from configuracao import *

 
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
    
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
 
atendimento_fields = {
    'empresa': fields.String,
    'pessoa': fields.String,
    'email': fields.String,
    'relato': fields.String,
    'data_cadastro': fields.DateTime,
    'data_atendimento': fields.DateTime,
    'observacao': fields.String,
    'categoria': fields.String,
    'satisfacao': fields.String,
    'satisfacao_observacao': fields.String,
    'retornar': fields.String,
    'ativo': fields.String,
    'uri': fields.Url('atendimento')
}


class atendimentos_api(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('empresa', type=str, required=True, help='Nenhuma Empresa foi passada!', location='json')
        self.reqparse.add_argument('meio', type=str, default="TELEFONE", location='json')
        super(atendimentos_api, self).__init__()
        
    def get(self):
        atendimento = Atendimento.query.filter(Atendimento.ativo=='SIM')
        return { 'atendimentos': map(lambda t: marshal(t, atendimento_fields), atendimento) }

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
        return { 'atendimento': marshal(atendimento, atendimento_fields) }, 201









class TaskAPI(Resource):
    decorators = [auth.login_required]
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        return { 'task': marshal(task[0], task_fields) }
        
    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v
        return { 'task': marshal(task, task_fields) }

    def delete(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return { 'result': True }

api.add_resource(atendimentos_api, '/atendimentos', endpoint = 'atendimentos')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'task')
    
if __name__ == '__main__':
    init_db()
    app.run(debug = True)