
### Slide 1

- SQLModel:
	**A Fusão:** É uma biblioteca que combina **SQLAlchemy** (ORM) e **Pydantic** (Validação de Dados).

- Sintaxe Básica:
	
		class Aluno(SQLModel, table=True):
	    id: int | None = Field(default=None, primary_key=True)
	    nome: str

- Sessão, comandos basicos:
	 **Criar:** `session.add(obj)`, `session.commit()`, `session.refresh(obj)` .
	 **Ler:** `session.exec(select(Modelo)).all()`.

**Atributo `Relationship`:** Define a conexão no nível do objeto (não cria coluna no banco, isso é o `foreign_key` dentro do `Field`).
**`back_populates`:** Parâmetro obrigatório para que a relação funcione nos "dois sentidos" (ex: User sabe seus Posts, Post sabe seu User)

se tiver uma relação de N pra N, precisa-se de uma tabela extra

**N para N:** Exige uma **Tabela Associativa** (Link Model). No SQLModel, usa-se `link_model=TabelaAssociativa` dentro do `Relationship`