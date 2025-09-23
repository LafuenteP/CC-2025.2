#Leia do teclado e escreva cada linha em arquivo de saída

import sys

linha = sys.stdin.readline()

while linha.strip() != "exit":
    with open("../Arquivos/saidaExercicio.txt","a", encoding="utf-8") as file:
        file.write(linha)
    linha = sys.stdin.readline()