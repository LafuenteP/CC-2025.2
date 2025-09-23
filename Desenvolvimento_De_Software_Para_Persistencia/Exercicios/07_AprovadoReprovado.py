import pandas as pd

alunos_df = pd.read_csv("../Arquivos/Alunos.csv")

#modifique a função para que agora crie:
# A situação "Aprovado", caso nota > 7
# A situação "Reprovado", caso nota < 4
# A situação "Recuperação", caso contrário

def situacaoAluno(Nota):
    if Nota > 7:
        return "Aprovado"
    elif Nota < 4:
        return "Reprovado"
    else:
        return "Recuperação"
    
alunos_df["Situacao"] = alunos_df["Nota"].apply(situacaoAluno)

print(alunos_df)