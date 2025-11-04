import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()

alunos_df = pd.DataFrame(columns=["nota"])


@app.post("/alunos")
def adicionar_ou_atualizar_aluno(nome: str, nota: float):
    
    global alunos_df 
    
    mensagem_status = ""

    if nome in alunos_df.index:
        mensagem_status = f"Nota do aluno '{nome}' foi atualizada."
    else:
        mensagem_status = f"Aluno '{nome}' foi registrado com sucesso."

    alunos_df.loc[nome, 'nota'] = nota

    return {
        "MSG": mensagem_status,
        "AlunoRegistrado": {
            "nome": nome,
            "nota": nota
        }
    }


@app.get("/alunos")
def listar_alunos_completo():

    df_para_json = alunos_df.reset_index()
    
    df_para_json = df_para_json.rename(columns={'index': 'nome'})

    return df_para_json.to_dict(orient="records")

@app.get("/alunos/{nome}")
def obter_nota_aluno(nome: str):
    
    if nome in alunos_df.index:
        
        nota_aluno = float(alunos_df.loc[nome, 'nota'])
        
        return {
            "nome": nome,
            "nota": nota_aluno
        }
    
    else:

        raise HTTPException(status_code=404, detail="Aluno inexistente.")
