from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

contador_id = 1
alunos_df = pd.DataFrame(columns=["id", "nome", "curso", "IRA"])

#Iniciando meu APP
app = FastAPI()

class Aluno(BaseModel):
    Nome : str
    Curso : str
    IRA : float

@app.post("/alunos")

def criar_Aluno( aluno: Aluno):
    global contador_id,alunos_df #preciso descriminar que é global, pois a linguagem é interpretada.
    novo = {
        "id" : contador_id,
        "nome" : aluno.Nome,
        "curso" : aluno.Curso,
        "IRA" : aluno.IRA

    }
    alunos_df = alunos_df._append(novo, ignore_index = True)
    contador_id += 1

    return {
        "MSG" : "Aluno Criado com Sucesso!",
        "Aluno" : novo
    }

#Os apps configuram as rotas dos serviços
@app.get("/alunos")
def listar_Alunos():
    return alunos_df.to_dict(orient="records")