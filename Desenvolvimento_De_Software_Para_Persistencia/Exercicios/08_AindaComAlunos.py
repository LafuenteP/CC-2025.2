import pandas as pd

alunos_df = pd.read_csv("../Arquivos/Alunos.csv")

nota_maxima = alunos_df["Nota"].max()
print("\nNota máxima: ", nota_maxima)

aluno_nota_maxima = alunos_df[alunos_df["Nota"] == nota_maxima]

print(aluno_nota_maxima)


# Alunos acima da média

media_notas = round(alunos_df["Nota"].mean(),2)
print("\nMédia geral: ", media_notas)

alunos_acima_da_media = alunos_df[alunos_df["Nota"] > media_notas]

print(alunos_acima_da_media)