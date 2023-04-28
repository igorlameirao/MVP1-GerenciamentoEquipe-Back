from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from entities import Equipe, Session
from dtos.request import EquipeReqModel

from controllers.equipe_controller import include_route as equipe_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


equipe_controller(app)