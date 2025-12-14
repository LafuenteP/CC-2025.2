import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import threading
import os
import random
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# --- Configuração do CORS ---
# Precisamos permitir que o navegador (rodando o index.html)
# acesse a API (rodando no 127.0.0.1)

origins = [
    "*", 
]

#Permitindo conexões
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Quais origens podem se conectar
    allow_credentials=True,      # Permite cookies (se houver)
    allow_methods=["*"],         # Permite todos os métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],         # Permite todos os cabeçalhos
)


PRODUTOS_CSV = "produtos.csv"

# impede que duas requisições tentem escrever no arquivo ao mesmo tempo
db_lock = threading.Lock()

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float

ultimo_id = 0


def carregar_dados():
    """
    Carrega os dados do CSV para um DataFrame do Pandas.
    Esta função é chamada DENTRO de um 'with db_lock:'
    """
    global ultimo_id
    try:
        df = pd.read_csv(PRODUTOS_CSV)
        if not df.empty:
            df['id'] = df['id'].astype(int)
            ultimo_id = int(df['id'].max()) 
        else:
            ultimo_id = 0
            df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])
            
    except FileNotFoundError:
        # Se o arquivo não existe, cria um DataFrame vazio
        df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])
        ultimo_id = 0
    
    # Garante que os tipos de dados estejam corretos
    df['preco'] = pd.to_numeric(df['preco'], errors='coerce').fillna(0.0)
    df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)
    
    return df

def salvar_dados(df: pd.DataFrame):

    df.to_csv(PRODUTOS_CSV, index=False)

@app.on_event("startup")
def popular_db_inicial():
    """
    Ao iniciar a API, verifica se o CSV tem dados suficientes.
    Se não tiver, popula com 30+ registros falsos.
    """
    print("API iniciando... Verificando banco de dados...")
    with db_lock: # Trava o acesso durante a verificação inicial
        df = carregar_dados()
        
        if len(df) < 30:
            print(f"Banco de dados com apenas {len(df)} registros. Populando com 35 registros...")
            
            # Limpa o dataframe para recomeçar (caso tenha dados parciais)
            df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])
            

            
            produtos = [
                {"nome": "Smartphone Galaxy S23", "categoria": "Eletrônicos"},
                {"nome": "Notebook Dell Inspiron 15", "categoria": "Eletrônicos"},
                {"nome": "Smart TV LG 50 polegadas 4K", "categoria": "Eletrônicos"},
                {"nome": "Fone de Ouvido Bluetooth Sony WH-1000XM5", "categoria": "Eletrônicos"},
                {"nome": "Mouse sem Fio Logitech MX Master 3", "categoria": "Eletrônicos"},
                {"nome": "Teclado Mecânico Redragon Kumara", "categoria": "Eletrônicos"},
                {"nome": "Monitor Gamer AOC Hero 27'' 144Hz", "categoria": "Eletrônicos"},
                
                {"nome": "Camiseta Básica Algodão (Branca)", "categoria": "Roupas"},
                {"nome": "Calça Jeans Masculina Slim", "categoria": "Roupas"},
                {"nome": "Tênis de Corrida Nike Pegasus 40", "categoria": "Roupas"},
                {"nome": "Jaqueta Corta-Vento Impermeável", "categoria": "Roupas"},
                {"nome": "Vestido Floral de Verão", "categoria": "Roupas"},
                {"nome": "Moletom com Capuz (Preto)", "categoria": "Roupas"},
                
                {"nome": "Arroz Integral 1kg", "categoria": "Alimentos"},
                {"nome": "Feijão Carioca 1kg", "categoria": "Alimentos"},
                {"nome": "Azeite de Oliva Extra Virgem 500ml", "categoria": "Alimentos"},
                {"nome": "Café em Grãos Especial 250g", "categoria": "Alimentos"},
                {"nome": "Chocolate Amargo 70% Cacau", "categoria": "Alimentos"},
                
                {"nome": "Furadeira de Impacto Bosch 650W", "categoria": "Ferramentas"},
                {"nome": "Kit de Chaves de Fenda (8 peças)", "categoria": "Ferramentas"},
                {"nome": "Alicate Universal Tramontina", "categoria": "Ferramentas"},
                {"nome": "Trena a Laser 40m", "categoria": "Ferramentas"},
            
                {"nome": "Bicicleta Aro 29 Mountain Bike", "categoria": "Esportes"},
                {"nome": "Bola de Futebol Oficial (Campo)", "categoria": "Esportes"},
                {"nome": "Tapete de Yoga em PVC", "categoria": "Esportes"},
                {"nome": "Kit Halteres 10kg", "categoria": "Esportes"},
            
                {"nome": "Livro: O Hobbit - J.R.R. Tolkien", "categoria": "Livros"},
                {"nome": "Livro: A Sutil Arte de Ligar o F*da-se", "categoria": "Livros"},
                {"nome": "Livro: 1984 - George Orwell", "categoria": "Livros"},
                
                {"nome": "Cadeira de Escritório Ergonômica", "categoria": "Móveis"},
                {"nome": "Mesa de Jantar 4 Lugares (Madeira)", "categoria": "Móveis"},
                {"nome": "Sofá Retrátil 3 Lugares (Cinza)", "categoria": "Móveis"},
                {"nome": "Guarda-Roupa Casal 6 Portas", "categoria": "Móveis"},
                {"nome": "Estante para Livros (Branca)", "categoria": "Móveis"}
            ] # Total: 35 produtos
            
            novos_produtos = []
            
            for i, produto in enumerate(produtos, start=1):
                novo_produto_com_preco = {
                    "id": i,
                    "nome": produto["nome"],
                    "categoria": produto["categoria"],
                    "preco": round(random.uniform(10.5, 999.9), 2) #preço aleatório
                }
                novos_produtos.append(novo_produto_com_preco)


     
            df_novos = pd.DataFrame(novos_produtos)
            df_final = pd.concat([df, df_novos], ignore_index=True)
            
            salvar_dados(df_final)
            
            # Atualiza o ultimo_id global corretamente
            global ultimo_id
            ultimo_id = int(df_final['id'].max()) # Converte para int
            print(f"Banco de dados populado. Total de {len(df_final)} registros. Último ID: {ultimo_id}")
        else:
            print(f"Banco de dados já está populado com {len(df)} registros. Último ID: {ultimo_id}")



#API (CRUD)

@app.post("/produtos", response_model=dict)
def cadastrar_produto(produto: Produto):
    """
    Cadastra um novo produto. Operação de escrita (usa lock).
    """
    with db_lock:
        df = carregar_dados()
        
        global ultimo_id
        ultimo_id += 1
        
        #adicionar UM produto
        novo_produto = {
            "id": int(ultimo_id), 
            "nome": produto.nome,
            "categoria": produto.categoria,
            "preco": float(produto.preco)
        }
        
        df_novo = pd.DataFrame([novo_produto])
        df_final = pd.concat([df, df_novo], ignore_index=True)
        
        salvar_dados(df_final)
        
        return novo_produto
    

@app.get("/produtos")
def listar_produtos():
    """
    Lista todos os produtos. Operação de leitura (usa lock para consistência).
    """
    with db_lock:
        df = carregar_dados()
        return df.to_dict(orient="records")

@app.get("/produtos/{id}")
def obter_produto(id: int):
    """
    Obtém um produto específico pelo ID. Leitura (usa lock).
    """
    with db_lock:
        df = carregar_dados()
        produto = df[df["id"] == id]
        
        if produto.empty:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        produto_dict = produto.to_dict(orient="records")[0]
        produto_dict['id'] = int(produto_dict['id'])
        produto_dict['preco'] = float(produto_dict['preco'])
        
        return produto_dict

@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):
    """
    Atualiza um produto existente. Escrita (usa lock).
    """
    with db_lock:
        df = carregar_dados()
        
        if id not in df["id"].values:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        # Atualiza os valores na linha correspondente
        df.loc[df["id"] == id, ["nome", "categoria", "preco"]] = [
            produto.nome, produto.categoria, produto.preco
        ]
        
        salvar_dados(df)
        
        produto_atualizado_dict = df[df["id"] == id].to_dict(orient="records")[0]
        produto_atualizado_dict['id'] = int(produto_atualizado_dict['id'])
        produto_atualizado_dict['preco'] = float(produto_atualizado_dict['preco'])
        return produto_atualizado_dict

@app.delete("/produtos/{id}")
def apagar_produto(id: int):
    """
    Apaga um produto. Escrita (usa lock).
    """
    with db_lock:
        df = carregar_dados()
        
        if id not in df["id"].values:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        # Pega os índices a serem removidos
        indices_para_apagar = df[df["id"] == id].index
        
        # Remove do dataframe
        df_atualizado = df.drop(indices_para_apagar).reset_index(drop=True)
        
        salvar_dados(df_atualizado)
        
        return {"mensagem": "Produto removido com sucesso"}



@app.get("/produtos/stats/maior-preco")
def obter_maior_preco():
    """
    Serviço 1: Produto de maior preço.
    """
    with db_lock:
        df = carregar_dados()
        if df.empty:
            raise HTTPException(status_code=404, detail="Não há produtos cadastrados.")
        
        # Encontra o índice do produto com maior preço
        idx_max = df['preco'].idxmax()
        produto_mais_caro = df.loc[idx_max]
        
        produto_dict = produto_mais_caro.to_dict()
        produto_dict['id'] = int(produto_dict['id'])
        produto_dict['preco'] = float(produto_dict['preco'])
        return produto_dict

@app.get("/produtos/stats/menor-preco")
def obter_menor_preco():
    """
    Serviço 2: Produto de menor preço.
    """
    with db_lock:
        df = carregar_dados()
        if df.empty:
            raise HTTPException(status_code=404, detail="Não há produtos cadastrados.")
            
        # Encontra o índice do produto com menor preço
        idx_min = df['preco'].idxmin()
        produto_mais_barato = df.loc[idx_min]
        
        produto_dict = produto_mais_barato.to_dict()
        produto_dict['id'] = int(produto_dict['id'])
        produto_dict['preco'] = float(produto_dict['preco'])
        return produto_dict

@app.get("/produtos/stats/media-preco")
def obter_media_preco():
    """
    Serviço 3: Média de preços.
    """
    with db_lock:
        df = carregar_dados()
        if df.empty:
            return {"media_preco": 0.0}
            
        media = df['preco'].mean()

        return {"media_preco": float(round(media, 2))}

@app.get("/produtos/stats/acima-media")
def obter_produtos_acima_media():
    """
    Serviço 4: Lista de produtos com preço maior ou igual à média.
    """
    with db_lock:
        df = carregar_dados()
        if df.empty:
            return []
            
        media = df['preco'].mean()
        produtos_acima_media = df[df['preco'] >= media]
        
        return produtos_acima_media.to_dict(orient="records")

@app.get("/produtos/stats/abaixo-media")
def obter_produtos_abaixo_media():
    """
    Serviço 5: Lista de produtos com preço abaixo da média.
    """
    with db_lock:
        df = carregar_dados()
        if df.empty:
            return []
            
        media = df['preco'].mean()
        produtos_abaixo_media = df[df['preco'] < media]
        
        return produtos_abaixo_media.to_dict(orient="records")
