# coding=utf-8
from sqlalchemy import Column, Integer, String, TIMESTAMP, TEXT
from database import Base
from colaboradores.models.py import Colaborador

class Atendimento(Base):
    __tablename__ = 'atendimentos'

    id = Column(Integer, primary_key=True)
    id_colaborador = Column(Integer, ForeignKey("colaborador.id"), nullable=False)
    empresa = Column(String(100))
    pessoa = Column(String(100))
    email = Column(String(100))
    meio = Column(String(100))
    relato = Column(TEXT)
    data_cadastro = Column(TIMESTAMP, default=time_now)
    data_atendimento = Column(TIMESTAMP, default=time_now)
    observacao = Column(TEXT)
    categoria = Column(String(100), default='SEM CATEGORIA')
    satisfacao = Column(Integer, default='4')
    satisfacao_observacao = Column(TEXT)
    retornar = Column(String(3), default='NÃO')
    ativo = Column(String(3), default='SIM')

    def __init__(self):
        self.ativo = 'SIM'

    def __repr__(self):
        return '<Atendimento %r %r %r>' % (self.empresa, self.pessoa, self.meio)