from fastapi import FastAPI, APIRouter

from dtos.request import EquipeReqModel
from entities import Equipe, Session

router = APIRouter(prefix='/equipes', tags=["Equipes"])


@router.post("")
def criar_equipe(model: EquipeReqModel):
    equipe = Equipe(nome=model.nome, apelido=model.apelido, cor_predominante=model.corPredominante)
    session = Session()
    session.add(equipe)
    session.commit()
    equipes = session.query(Equipe).all()
    return equipes

@router.delete("")
def excluir_equipe(id: int):
    session = Session()
    equipe = session.query(Equipe).filter(Equipe.id == id).first()
    session.delete(equipe)
    session.commit()
    return {"success": True, "message": "Equipe criado com sucesso!"}

@router.get("")
def get_equipes():
    session = Session()
    equipes = session.query(Equipe).all()
    return equipes


@router.get("/{id}")
def get_equipes_by_id(id: int):
    session = Session()
    equipe = session.query(Equipe).filter(Equipe.id == id).first()
    return equipe


@router.put("")
def alterar(model: EquipeReqModel):
    session = Session()
    session.query(Equipe).filter(Equipe.id == model.id)\
        .update({'nome': model.nome, 'apelido': model.apelido, 'cor_predominante': model.corPredominante})
    session.commit()
    equipes = session.query(Equipe).all()
    return equipes








'''
@router.post("")
def create_equipe(model: EquipeReqModel):
    print(model.nome + model.sigla)
    equipe = Equipe(nome=model.nome, sigla=model.sigla)
    session = Session()
    session.add(equipe)
    session.commit()
    return {"success": True, "message": "Equipe criado com sucesso!"}

'''

def include_route(app: FastAPI):
    app.include_router(router)
