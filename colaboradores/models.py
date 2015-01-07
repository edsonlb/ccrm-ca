# coding=utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from database import Base
from atendimentos.models import *
from flask.ext.restful import fields

class Colaborador(Base):
    __tablename__ = 'colaboradores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, unique=True)
    avatar = Column(String(100), default='avatar.png')
    email = Column(String(100),index=True, nullable=False)
    skype = Column(String(100))
    hangout = Column(String(100))
    telefone = Column(String(100))
    senha = Column(String(100),index=True, default='senha')
    ativo = Column(String(3),index=True, default='SIM')
    atendimentos = relationship('Atendimento', backref='colaborador', lazy='dynamic')

    def __init__(self):
        self.ativo = 'SIM'

    def __repr__(self):
        return '<Colaborador %r>' % (self.nome)

# marshallers
colaborador_campos = {
    'id': fields.Integer,
    'nome': fields.String,
    'avatar': fields.String,
    'email': fields.String,
    'skype': fields.String,
    'hangout': fields.String,
    'telefone': fields.String,
    'senha': fields.String,
    'ativo': fields.String
    
}

#'uri': fields.Url('colaborador')