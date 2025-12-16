from fastapi import FastAPI
from app.routes import cursos, professores, disciplinas, alunos, dashboard

app = FastAPI(title="Sistema Acadêmico API", version="1.0.0")

# Aqui a gente avisa o App que as rotas de cursos existem
app.include_router(cursos.router)
app.include_router(professores.router)
app.include_router(disciplinas.router)
app.include_router(alunos.router)
app.include_router(dashboard.router) 

@app.get("/")
def root():
    return {"mensagem": "API Funcionando! Acesse /docs para usar."}