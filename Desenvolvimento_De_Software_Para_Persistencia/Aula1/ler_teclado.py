import sys

linha = sys.stdin.readline()

while linha:
    print("-->"+linha.strip()+"<--")
    linha = sys.stdin.readline()

#se não tivesse o strip, quando eu digito espaços antes de depois do conteúdo
#ele não reduziria a string para as setas ficarem "coladas"