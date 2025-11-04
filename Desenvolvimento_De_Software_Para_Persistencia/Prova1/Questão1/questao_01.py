
soma_notas = 0.0
total_alunos = 0

maior_nota = 0.0 
nome_maior_nota = ""
menor_nota = float('inf') 
nome_menor_nota = ""


with open("dados_alunos.txt", "r") as file:
    linha = file.readline()
    while(linha):
        linha_limpa = linha.strip()
        dados_aluno = linha_limpa.split('#')
        if len(dados_aluno) == 3:
            nome = dados_aluno[0]
            nota_str = dados_aluno[2]
            nota = float(nota_str)
                    
            soma_notas += nota
            total_alunos += 1
                    
            if nota > maior_nota:
                maior_nota = nota
                nome_maior_nota = nome
                        
            if nota < menor_nota:
                menor_nota = nota
                nome_menor_nota = nome
                        
            
        linha = file.readline()


media_turma = soma_notas / total_alunos
        
print(f"Média da turma: {media_turma:.2f}")
print(f"Maior nota: {maior_nota} ({nome_maior_nota})")
print(f"Menor nota: {menor_nota} ({nome_menor_nota})")
    
