from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_session
from app.models import Aluno, Matricula, Disciplina

router = APIRouter(prefix="/alunos", tags=["Alunos"])

# --- CRUD BÁSICO ---

@router.post("/", response_model=Aluno)
def criar_aluno(aluno: Aluno, session: Session = Depends(get_session)):
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno

@router.get("/", response_model=List[Aluno])
def listar_alunos(session: Session = Depends(get_session)):
    return session.exec(select(Aluno)).all()

# --- A MÁGICA DO MANY-TO-MANY ---

@router.post("/{aluno_id}/matricular/{disciplina_id}")
def matricular_aluno(aluno_id: int, disciplina_id: int, session: Session = Depends(get_session)):
    # 1. Verifica se Aluno existe
    aluno = session.get(Aluno, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    # 2. Verifica se Disciplina existe
    disciplina = session.get(Disciplina, disciplina_id)
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    
    # 3. Cria o link entre eles
    matricula = Matricula(aluno_id=aluno_id, disciplina_id=disciplina_id)
    
    session.add(matricula)
    try:
        session.commit()
    except Exception as e:
        # Pega erro se já estiver matriculado (Unique constraint)
        raise HTTPException(status_code=400, detail="Erro ao matricular. Talvez já esteja matriculado?")
        
    return {"mensagem": f"Aluno {aluno.nome} matriculado em {disciplina.nome} com sucesso!"}

# Consulta Complexa: Ver disciplinas de um aluno específico
@router.get("/{aluno_id}/disciplinas")
def listar_disciplinas_do_aluno(aluno_id: int, session: Session = Depends(get_session)):
    aluno = session.get(Aluno, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    # O SQLModel faz a mágica aqui graças ao relacionamento no models.py
    return aluno.disciplinas