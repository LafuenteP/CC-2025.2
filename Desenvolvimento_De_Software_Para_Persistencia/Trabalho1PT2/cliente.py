import httpx
import time
import json

BASE_URL = "http://127.0.0.1:8000"

def print_json(data):
    """Imprime o JSON formatado de forma legível."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def testar_listar_produtos():
    print("\n--- [TESTE] GET /produtos (Listar Todos) ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print(f"Total de produtos: {len(resp.json())}")

    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_cadastrar_produto():
    print("\n--- [TESTE] POST /produtos (Cadastrar Novo) ---")
    produto_novo = {
        "nome": "Produto Teste via Cliente",
        "categoria": "Testes",
        "preco": 99.99
    }
    try:
        resp = httpx.post(f"{BASE_URL}/produtos", json=produto_novo)
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Produto cadastrado:")
        print_json(resp.json())
        return resp.json().get("id") # Retorna o ID do produto criado
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")
    return None

def testar_obter_produto(id: int):
    print(f"\n--- [TESTE] GET /produtos/{id} (Obter Um) ---")
    if not id:
        print("ID inválido para teste.")
        return
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/{id}")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print(f"Dados do produto {id}:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_atualizar_produto(id: int):
    print(f"\n--- [TESTE] PUT /produtos/{id} (Atualizar) ---")
    if not id:
        print("ID inválido para teste.")
        return
    
    produto_att = {
        "nome": "Produto Teste ATUALIZADO",
        "categoria": "Testes-ATT",
        "preco": 123.45
    }
    try:
        resp = httpx.put(f"{BASE_URL}/produtos/{id}", json=produto_att)
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Produto atualizado:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_apagar_produto(id: int):
    print(f"\n--- [TESTE] DELETE /produtos/{id} (Apagar) ---")
    if not id:
        print("ID inválido para teste.")
        return
    try:
        resp = httpx.delete(f"{BASE_URL}/produtos/{id}")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Resposta:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

#Testes de Estatísticas

def testar_maior_preco():
    print("\n--- [TESTE] GET /produtos/stats/maior-preco ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/stats/maior-preco")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Produto mais caro:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_menor_preco():
    print("\n--- [TESTE] GET /produtos/stats/menor-preco ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/stats/menor-preco")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Produto mais barato:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_media_preco():
    print("\n--- [TESTE] GET /produtos/stats/media-preco ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/stats/media-preco")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print("Média de preços:")
        print_json(resp.json())
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_acima_media():
    print("\n--- [TESTE] GET /produtos/stats/acima-media ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/stats/acima-media")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print(f"Total de produtos acima da média: {len(resp.json())}")
        # print("Amostra:")
        # print_json(resp.json()[:3])
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")

def testar_abaixo_media():
    print("\n--- [TESTE] GET /produtos/stats/abaixo-media ---")
    try:
        resp = httpx.get(f"{BASE_URL}/produtos/stats/abaixo-media")
        resp.raise_for_status()
        print(f"Status: {resp.status_code}")
        print(f"Total de produtos abaixo da média: {len(resp.json())}")
        # print("Amostra:")
        # print_json(resp.json()[:3])
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Erro ao conectar na API: {e}")


if __name__ == "__main__":
    print("Iniciando suíte de testes do cliente da API...")
    print(f"API alvo: {BASE_URL}")
    print("="*50)
    
    # Testando CRUD
    testar_listar_produtos()
    time.sleep(1)
    
    id_criado = testar_cadastrar_produto()
    time.sleep(1)
    
    if id_criado:
        testar_obter_produto(id_criado)
        time.sleep(1)
        
        testar_atualizar_produto(id_criado)
        time.sleep(1)
        
        # Obtém de novo para ver se atualizou
        testar_obter_produto(id_criado) 
        time.sleep(1)
        
        testar_apagar_produto(id_criado)
        time.sleep(1)
        
        # Tenta obter o produto apagado (deve falhar)
        testar_obter_produto(id_criado)
        time.sleep(1)

    print("\n" + "="*50)
    print("Iniciando testes dos serviços de estatísticas...")
    print("="*50)

    # Testando Estatísticas
    testar_maior_preco()
    time.sleep(1)
    
    testar_menor_preco()
    time.sleep(1)
    
    testar_media_preco()
    time.sleep(1)
    
    testar_acima_media()
    time.sleep(1)
    
    testar_abaixo_media()
    
    print("\n" + "="*50)
    print("Suíte de testes finalizada.")