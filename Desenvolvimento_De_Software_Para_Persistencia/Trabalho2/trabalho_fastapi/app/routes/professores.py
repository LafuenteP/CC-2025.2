from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_session
from app.models import Professor

router = APIRouter(prefix="/professores", tags=["Professores"])

@router.post("/", response_model=Professor)
def criar_professor(professor: Professor, session: Session = Depends(get_session)):
    session.add(professor)
    session.commit()
    session.refresh(professor)
    return professor

@router.get("/", response_model=List[Professor])
def listar_professores(session: Session = Depends(get_session)):
    return session.exec(select(Professor)).all()