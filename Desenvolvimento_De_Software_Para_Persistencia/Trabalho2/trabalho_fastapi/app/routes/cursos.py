from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models import Curso

router = APIRouter(prefix="/cursos", tags=["Cursos"])

# 1. CRIAR CURSO (Create)
@router.post("/", response_model=Curso)
def criar_curso(curso: Curso, session: Session = Depends(get_session)):
    session.add(curso)
    session.commit()
    session.refresh(curso)
    return curso

# 2. LISTAR CURSOS (Read)
@router.get("/", response_model=List[Curso])
def listar_cursos(session: Session = Depends(get_session)):
    statement = select(Curso)
    results = session.exec(statement).all()
    return results

# 3. BUSCAR POR ID
@router.get("/{curso_id}", response_model=Curso)
def obter_curso(curso_id: int, session: Session = Depends(get_session)):
    curso = session.get(Curso, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso