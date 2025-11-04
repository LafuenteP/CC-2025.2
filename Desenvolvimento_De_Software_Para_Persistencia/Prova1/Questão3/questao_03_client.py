import httpx
import sys

BASE_URL = "http://127.0.0.1:8000"

def adicionar_ou_atualizar(nome_aluno: str, nota_aluno: float):

    print("-" * 40)
    print(f"Tentando registrar: {nome_aluno} com nota {nota_aluno}")
    
    try:
        response = httpx.post(
            f"{BASE_URL}/alunos",
            params={
                "nome": nome_aluno,
                "nota": nota_aluno
            }
        )
        
        response.raise_for_status() 
        
        print(response.json()["MSG"])
        print(f"Dados: {response.json()['AlunoRegistrado']}")

    except httpx.HTTPStatusError as exc:
        print(f"Erro HTTP ao tentar registrar: {exc.response.status_code} - {exc.response.text}")
    except httpx.ConnectError:
        print(f"ERRO: Não foi possível conectar à API em {BASE_URL}")
        print("Por favor, verifique se o servidor FastAPI (questao_03.py) está rodando.")
        sys.exit(1) # Interrompe o cliente

def buscar_aluno(nome_aluno: str):
  
    print("-" * 40)
    print(f"Tentando buscar: {nome_aluno}")
    
    try:
        response = httpx.get(f"{BASE_URL}/alunos/{nome_aluno}")
        
        response.raise_for_status()
        
        print(f"Aluno encontrado: {response.json()}")
        
    except httpx.HTTPStatusError as exc:

        if exc.response.status_code == 404:
            print(f"Resultado: Aluno '{nome_aluno}' não foi registrado.")
        else:
            print(f"Erro HTTP inesperado ao buscar: {exc.response.status_code}")
    except httpx.ConnectError:
        print("ERRO: API não está respondendo.")
        sys.exit(1)

def listar_alunos():
    
    try:
        response = httpx.get(f"{BASE_URL}/alunos")

        response.raise_for_status()

        print(f"Alunos encontrados: {response.json()}")

    except httpx.HTTPStatusError as exc:
        print(f"Erro HTTP ao listar alunos: {exc.response.status_code} - {exc.response.text}")
    except httpx.ConnectError:
        print(f"ERRO: Não foi possível conectar à API em {BASE_URL}")
        sys.exit(1)


# 1. Adicionando alunos
adicionar_ou_atualizar(nome_aluno="Ana", nota_aluno=9.5)
adicionar_ou_atualizar(nome_aluno="Bruno", nota_aluno=7.2)
adicionar_ou_atualizar(nome_aluno="Carla", nota_aluno=8.0)

# 2. Buscando um aluno
buscar_aluno(nome_aluno="Bruno")

# 3. Atualizando a nota de um aluno existente
adicionar_ou_atualizar(nome_aluno="Ana", nota_aluno=10.0)

# 4. Buscando o aluno com a nota atualizada
buscar_aluno(nome_aluno="Ana")

# 5. Buscando um aluno que não existe (deve falhar com 404)
buscar_aluno(nome_aluno="Zeca")

listar_alunos()