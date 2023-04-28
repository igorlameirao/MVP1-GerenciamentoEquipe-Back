from pydantic import BaseModel

class EquipeReqModel(BaseModel):
    id: int
    nome: str
    apelido: str
    corPredominante: str