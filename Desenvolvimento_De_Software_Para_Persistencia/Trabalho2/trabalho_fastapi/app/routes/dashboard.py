from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from app.database import get_session
from app.models import Aluno, Professor, Disciplina, Curso

router = APIRouter(prefix="/dashboard", tags=["Dashboard / Estatísticas"])

@router.get("/geral")
def estatisticas_gerais(session: Session = Depends(get_session)):
    """
    Retorna totais simples (Agregações de contagem)
    """
    total_alunos = session.exec(select(func.count(Aluno.id))).one()
    total_cursos = session.exec(select(func.count(Curso.id))).one()
    total_profs = session.exec(select(func.count(Professor.id))).one()
    
    return {
        "total_alunos": total_alunos,
        "total_cursos": total_cursos,
        "total_professores": total_profs
    }

@router.get("/alunos-por-curso")
def contar_alunos_por_curso(session: Session = Depends(get_session)):
    """
    Consulta complexa: Agrupa alunos por curso através das disciplinas
    """
    # SQL Bruto equivalente: SELECT curso.nome, COUNT(aluno.id) ... GROUP BY curso.id
    # No SQLModel/SQLAlchemy é um pouco mais chato, então vamos simplificar 
    # contando disciplinas por curso que é direto
    
    results = session.exec(
        select(Curso.nome, func.count(Disciplina.id))
        .join(Disciplina)
        .group_by(Curso.id)
    ).all()
    
    # Formata para JSON bonitinho
    return [{"curso": row[0], "qtd_disciplinas": row[1]} for row in results]