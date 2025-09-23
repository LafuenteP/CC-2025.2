import pandas as pd

# Use a mesma series que o exercício 3, porém imprima só as notas maiores que 7.0
#
# Dica: para filtrar uma Series use: "nome_series<operador>valor" como argumento do
# colchete da series original (nome_series)

notas_aluno = pd.Series([9.3, 7.4, 5.6], index = ["Biologia", "Matemática", "Geografia"])

print(notas_aluno[notas_aluno>7.0])