# coding=utf-8
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP, TEXT
from database import Base
from colaboradores.models import Colaborador
from datetime import datetime

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
        return '<Atendimento %r %r %r>' % (self.empresa, self.pessoa, self.meio)