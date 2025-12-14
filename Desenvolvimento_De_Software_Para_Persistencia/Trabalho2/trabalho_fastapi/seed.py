import random
from sqlmodel import Session, select
from app.database import engine
from app.models import Curso, Professor, Disciplina, Aluno, Matricula

def create_data():
    with Session(engine) as session:
        # 1. Criar Cursos
        cursos_nomes = ["Engenharia de Software", "Design Digital", "Ciência da Computação", "Sistemas de Informação"]
        cursos = []
        for nome in cursos_nomes:
            curso = Curso(nome=nome, descricao=f"Bacharelado em {nome}")
            session.add(curso)
            cursos.append(curso)
        session.commit()
        print(f"✅ {len(cursos)} Cursos criados.")

        # 2. Criar Professores
        professores = []
        nomes_profs = ["Ana Silva", "Carlos Souza", "Beatriz Lima", "Daniel Rocha", "Elena Alves", 
                       "Fabio Dias", "Gabriela Melo", "Hugo Costa", "Igor Santos", "Julia Pereira"]
        for nome in nomes_profs:
            prof = Professor(nome=f"Dr. {nome}", email=f"{nome.split()[0].lower()}@faculdade.edu.br")
            session.add(prof)
            professores.append(prof)
        session.commit()
        print(f"✅ {len(professores)} Professores criados.")

        # Recarregar objetos para garantir IDs
        for c in cursos: session.refresh(c)
        for p in professores: session.refresh(p)

        # 3. Criar Disciplinas (Ligadas a Cursos e Professores)
        disciplinas_nomes = [
            "Programação Web", "Banco de Dados", "Algoritmos", "Inteligência Artificial", 
            "Design de Interfaces", "Gestão de Projetos", "Estrutura de Dados", "Redes de Computadores",
            "Segurança da Informação", "Matemática Discreta", "Cálculo I", "Ética em TI"
        ]
        disciplinas = []
        for i, nome in enumerate(disciplinas_nomes):
            disc = Disciplina(
                nome=nome,
                ano=2025,
                semestre=(i % 2) + 1,
                curso_id=random.choice(cursos).id,
                professor_id=random.choice(professores).id
            )
            session.add(disc)
            disciplinas.append(disc)
        session.commit()
        print(f"✅ {len(disciplinas)} Disciplinas criadas.")

        # Recarregar disciplinas
        for d in disciplinas: session.refresh(d)

        # 4. Criar Alunos
        alunos = []
        nomes_alunos = ["Lucas", "Mateus", "Gabriel", "Larissa", "Fernanda", "Rafael", "Bruno", "Carla", 
                        "Mariana", "Thiago", "Vinicius", "Sara", "Renan", "Patrícia", "Otávio"]
        sobrenomes = ["Ferreira", "Gomes", "Martins", "Araujo", "Barbosa"]
        
        for i in range(40): # Criar 40 alunos
            nome_completo = f"{random.choice(nomes_alunos)} {random.choice(sobrenomes)}"
            aluno = Aluno(nome=nome_completo, matricula_numero=f"2025{i:04d}")
            session.add(aluno)
            alunos.append(aluno)
        session.commit()
        print(f"✅ {len(alunos)} Alunos criados.")

        # Recarregar alunos
        for a in alunos: session.refresh(a)

        # 5. Criar Matrículas (Many-to-Many)
        # Cada aluno se matricula em 3 disciplinas aleatórias
        count_matriculas = 0
        for aluno in alunos:
            disciplinas_escolhidas = random.sample(disciplinas, 3)
            for disc in disciplinas_escolhidas:
                matricula = Matricula(aluno_id=aluno.id, disciplina_id=disc.id)
                session.add(matricula)
                count_matriculas += 1
        
        session.commit()
        print(f"✅ {count_matriculas} Matrículas realizadas.")

if __name__ == "__main__":
    create_data()