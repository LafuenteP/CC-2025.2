import pandas as pd

alunos_df = pd.read_csv("../Arquivos/Alunos.csv")

# Criar uma nova coluna chamada "Situação", nela você deve calcular se
# o aluno foi aprovado ou não, (nota > 7). Se sim, a coluna deve ter o
# valor "Aprovado", caso contrário o valor deverá ser "Reprovado"

def situacaoAluno(Nota):
    if Nota > 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
alunos_df["Situacao"] = alunos_df["Nota"].apply(situacaoAluno)

print(alunos_df)