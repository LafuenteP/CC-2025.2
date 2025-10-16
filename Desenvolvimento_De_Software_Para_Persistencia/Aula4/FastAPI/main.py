from fastapi import FastAPI, HTTPException # Para minha API
from pydantic import BaseModel # Para descrever meu Modelo de aluno
import pandas as pd
#import time
#import asyncio

contador_id = 1
alunos_df = pd.DataFrame([])

class Aluno(BaseModel) :
    nome : str
    curso : str
    IRA : float


def criarAluno(aluno: Aluno): # Casei o tipo de entrada com o modelo "Aluno"
    novo = {
        "id" : contador_id,
        "nome" : aluno.nome

    }




