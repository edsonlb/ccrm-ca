#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://celul051_teste:teste@celuladigital.com.br/celul051_teste', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import colaboradores.models
    import atendimentos.models

    Base.metadata.create_all(bind=engine)