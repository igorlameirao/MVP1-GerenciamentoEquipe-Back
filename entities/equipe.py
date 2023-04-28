from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from entities import Base

class Equipe(Base):
    __tablename__ = 'equipe'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140))
    apelido = Column(String(140), unique=True)
    cor_predominante = Column(String(140))
    data_criacao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, apelido: str,cor_predominante: str ):
        self.nome = nome
        self.apelido = apelido
        self.cor_predominante = cor_predominante
