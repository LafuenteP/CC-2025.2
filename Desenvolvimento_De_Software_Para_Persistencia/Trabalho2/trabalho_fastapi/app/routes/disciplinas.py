from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from app.database import get_session
from app.models import Disciplina

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

# CREATE (Com chaves estrangeiras curso_id e professor_id)
@router.post("/", response_model=Disciplina)
def criar_disciplina(disciplina: Disciplina, session: Session = Depends(get_session)):
    # Opcional: Validar se curso e professor existem antes de criar
    session.add(disciplina)
    session.commit()
    session.refresh(disciplina)
    return disciplina

# READ (Com Filtros Requisitados: Ano e Texto Parcial)
@router.get("/", response_model=List[Disciplina])
def listar_disciplinas(
    session: Session = Depends(get_session),
    ano: Optional[int] = Query(None, description="Filtrar por ano de oferta"),
    nome: Optional[str] = Query(None, description="Filtrar por nome (busca parcial)")
):
    query = select(Disciplina)
    
    # Requisito d) Filtros por data/ano
    if ano:
        query = query.where(Disciplina.ano == ano)
    
    # Requisito c) Buscas por texto parcial
    if nome:
        query = query.where(Disciplina.nome.contains(nome))
        
    return session.exec(query).all()

# DELETE (Para garantir o CRUD completo)
@router.delete("/{id}")
def deletar_disciplina(id: int, session: Session = Depends(get_session)):
    disciplina = session.get(Disciplina, id)
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    session.delete(disciplina)
    session.commit()
    return {"ok": True}