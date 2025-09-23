import pandas as pd

df = pd.read_csv("../Arquivos/Alunos.csv")
#print(df)
#print(df.describe())
#print(df.head(2))

# Retornar um dataframe com os alunos cuja nota > 7 

#teste = pd.Series([True,True,False,False]) 
# Isso mostra que ao usar (df["Nota>7"]) ele tá usando os valores onde tem true e false para mostrar ou não

aprovados = df[df["Nota"] > 7]
#aprovados = df[teste]

#print(aprovados)


# Notas em ordem
notas_organizadas = df.sort_values("Nota", ascending=False)
print(notas_organizadas)

