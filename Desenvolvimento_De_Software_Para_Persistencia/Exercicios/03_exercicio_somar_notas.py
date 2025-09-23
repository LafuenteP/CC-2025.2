import pandas as pd

# Crie uma series com as seguintes notas do Aluno
# Biologia 9.3
# Matemática 7.4
# Geografia 5.6

# Em seguida você deve somar 0.5 em todas a notas de uma única vez
# Dica: Use series.add(valor), lembrando que essa operação não altera a original

notas_aluno = pd.Series([9.3, 7.4, 5.6], index = ["Biologia", "Matemática", "Geografia"])
print("\nNotas antes da adição:\n",notas_aluno, "\n")
adicao = pd.Series([0.5,0.5,0.5], index = ["Biologia", "Matemática", "Geografia"])
notas_adicionadas = notas_aluno.add(adicao)
print("Notas depois da adição:\n",notas_adicionadas)
