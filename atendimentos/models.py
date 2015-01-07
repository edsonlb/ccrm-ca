# coding=utf-8
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP, TEXT
from database import Base
from colaboradores.models import *
from datetime import datetime
from flask.ext.restful import fields

class Atendimento(Base):
    __tablename__ = 'atendimentos'

    id = Column(Integer, primary_key=True)
    id_colaborador = Column(Integer, ForeignKey("colaboradores.id"), nullable=False)
    empresa = Column(String(100), index=True)
    pessoa = Column(String(100))
    email = Column(String(100), index=True)
    meio = Column(String(100), index=True)
    relato = Column(TEXT)
    data_cadastro = Column(TIMESTAMP, default=datetime.now())
    data_atendimento = Column(TIMESTAMP, default=datetime.now())
    observacao = Column(TEXT)
    categoria = Column(String(100),index=True, default='SEM CATEGORIA')
    satisfacao = Column(Integer, default='4')
    satisfacao_observacao = Column(TEXT)
    retornar = Column(String(3), default='NÃO')
    ativo = Column(String(3),index=True, default='SIM')

    def __init__(self):
        self.ativo = 'SIM'

    def __repr__(self):
        return '<Atendimento %r>' % (self.pessoa)

# marshallers = http://stackoverflow.com/questions/22035974/flask-restful-marshal-complex-object-to-json
atendimento_campos = {
    'id': fields.Integer,
    'id_colaborador': fields.Nested(colaborador_campos),
    'empresa': fields.String,
    'pessoa': fields.String,
    'email': fields.String,
    'meio': fields.String,
    'relato': fields.String,
    'data_cadastro': fields.DateTime,
    'data_atendimento': fields.DateTime,
    'observacao': fields.String,
    'categoria': fields.String,
    'satisfacao': fields.String,
    'satisfacao_observacao': fields.String,
    'retornar': fields.String,
    'ativo': fields.String
    #'uri': fields.Url('atendimento')
}