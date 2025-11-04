import pandas as pd

receitas_semanais = pd.Series([12000, 17500, 14300, 16000, 19500], index = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"])


print(receitas_semanais)
print("-" * 40)

total_arrecadado = receitas_semanais.sum()
print(f"Total arrecadado: US$ {total_arrecadado}")

media_receitas = receitas_semanais.mean()
print(f"Média das receitas: US$ {media_receitas:.2f}")

nome_maior_arrecadador = receitas_semanais.idxmax()
valor_maior_arrecadador = receitas_semanais[nome_maior_arrecadador]
print(f"Associado que mais arrecadou: {nome_maior_arrecadador} (US$ {valor_maior_arrecadador})")


print("-" * 40)
print("Associados acima da média (operação booleana):")


associados_acima_da_media = receitas_semanais[receitas_semanais > media_receitas]

print(associados_acima_da_media)