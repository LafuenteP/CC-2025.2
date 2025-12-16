from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Tabela de Associação (Many-to-Many: Aluno <-> Disciplina)
class Matricula(SQLModel, table=True):
    aluno_id: Optional[int] = Field(default=None, foreign_key="aluno.id", primary_key=True)
    disciplina_id: Optional[int] = Field(default=None, foreign_key="disciplina.id", primary_key=True)

class Curso(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None
    
    disciplinas: List["Disciplina"] = Relationship(back_populates="curso")

class Professor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    
    disciplinas: List["Disciplina"] = Relationship(back_populates="professor")

class Disciplina(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    ano: int  # Para o requisito de filtro por ano
    semestre: int
    
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id")
    curso: Optional[Curso] = Relationship(back_populates="disciplinas")
    
    professor_id: Optional[int] = Field(default=None, foreign_key="professor.id")
    professor: Optional[Professor] = Relationship(back_populates="disciplinas")
    
    alunos: List["Aluno"] = Relationship(back_populates="disciplinas", link_model=Matricula)

class Aluno(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    matricula_numero: str
    
    disciplinas: List[Disciplina] = Relationship(back_populates="alunos", link_model=Matricula)