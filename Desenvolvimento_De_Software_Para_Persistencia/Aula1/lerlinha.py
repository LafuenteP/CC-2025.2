with open("../Arquivos/02_alunos.txt", "r") as file:
    linha = file.readline()
    while(linha):
        #strip() apara as arestas da string 'linha'
        print(linha.strip())
        linha = file.readline()
