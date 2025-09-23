import pandas as pd

dados = {
    "Nome": ["Ana","Lafuente","Nicolas","Évila"],
    "Idade": [23,35,45,29],
    "Cidade": ["São Paulo", "Fortaleza", "Rio de Janeiro", "Brejo Santo"]
}

#print(dados["Nome"])
#nome_series = pd.Series(dados["Nome"])

df = pd.DataFrame(dados)
print(df)

# Criando Series a partir de coluna:

coluna = pd.Series(df["Idade"])

print(coluna)

# Maior idade = df["Idade"].max()
# Menor idade = df["Idade"].min()