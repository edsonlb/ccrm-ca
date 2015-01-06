# coding=utf-8
from sqlalchemy import Column, Integer, String
from database import Base

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

    def __init__(self, nome=None, email=None, senha='senha'):
        self.name = name
        self.email = email
        self.senha = senha
        self.ativo = 'SIM'

    def __repr__(self):
        return '<Colaborador %r>' % (self.nome)