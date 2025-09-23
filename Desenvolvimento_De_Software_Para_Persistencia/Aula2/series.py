#Series no pandas é um array que responde por uma label
#como num array de notas que você chama pelo nome do aluno ao invés do índice.

import pandas as pd

#Series não rotuladas (com labels)
notas = pd.Series([7.5, 4.6, 9.2, 5.5])

#print(notas)

notasRotuladas = pd.Series([7.5, 4.6, 9.2, 5.5], index = ["João", "Thais", "Cintia", "Pedro"])

#Forma correta de acessar: notas.iloc[pos]

print(notasRotuladas["Thais"])

try:
    print(notasRotuladas["Bento"])
except Exception as e:
    print("Ocorreu uma exceção!", type(e).__name__)