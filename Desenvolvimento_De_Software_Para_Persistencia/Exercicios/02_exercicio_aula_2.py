# Exercício: Crie uma series chamada precos_frutas com o preço de 3 frutas:
# Maçã: 2.50
# Banana: 5.60
# Abacate: 6.30

# Imprima o preço da banana usando a chave. Depois imprima o mesmo preço usando o índice (iloc)

import pandas as pd

preco_frutas = pd.Series([2.50, 5.60, 6.30], ["Maçã", "Banana", "Abacate"])

print("Usando a chave:", preco_frutas["Banana"])

print("Usando o índice:", preco_frutas.iloc[1])