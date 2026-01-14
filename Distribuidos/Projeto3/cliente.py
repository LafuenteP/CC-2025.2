import json
import urllib.request
import urllib.error

# Configurações
URL_BASE = "http://localhost:8080"

def enviar_post(endpoint, dados):
    url = f"{URL_BASE}{endpoint}"
    dados_json = json.dumps(dados).encode('utf-8')
    
    req = urllib.request.Request(url, data=dados_json, method='POST')
    req.add_header('Content-Type', 'application/json')
    
    try:
        with urllib.request.urlopen(req) as response:
            resposta = response.read().decode('utf-8')
            return json.loads(resposta)
    except urllib.error.HTTPError as e:
        print(f"Erro {e.code}: {e.read().decode('utf-8')}")
        return None

print("--- Cliente Python: Sistema de Hotel ---")

# 1. Cadastrar Cliente
print("\n1. Cadastrando Cliente via Python...")
payload_cliente = {"nome": "Cliente Python", "cpf": "555.555.555-55"}
cliente = enviar_post("/clientes", payload_cliente)

if cliente:
    print(f"   Sucesso! Cliente cadastrado: ID {cliente['id']}, Nome: {cliente['nome']}")

    # 2. Fazer Reserva
    print("\n2. Tentando reservar quarto 101...")
    payload_reserva = {"cpf": "555.555.555-55", "quarto": 101}
    reserva = enviar_post("/reservas", payload_reserva)
    
    if reserva:
        print(f"   Reserva Realizada! ID: {reserva['idReserva']}, Status: {reserva['status']}")
    else:
        print("   Falha na reserva.")