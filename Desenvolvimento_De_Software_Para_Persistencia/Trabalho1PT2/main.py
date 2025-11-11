import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import threading
import os
from faker import Faker # Biblioteca para gerar dados falsos
import random

# --- Configuração Inicial ---

# 1. Inicializa o FastAPI
app = FastAPI()

# 2. Define o arquivo CSV que servirá como nosso banco de dados
PRODUTOS_CSV = "produtos.csv"

# 3. Cria um Lock (cadeado) para controlar o acesso concorrente ao arquivo CSV
# Isso impede que duas requisições tentem escrever no arquivo ao mesmo tempo,
# o que causaria corrupção de dados.
db_lock = threading.Lock()

# 4. Define o "schema" do nosso produto usando Pydantic
class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float

# 5. Variável global para manter o último ID (será carregado do CSV)
ultimo_id = 0

# --- Funções Auxiliares de Banco de Dados (CSV) ---

def carregar_dados():
    """
    Carrega os dados do CSV para um DataFrame do Pandas.
    Esta função é chamada DENTRO de um 'with db_lock:'
    """
    global ultimo_id
    try:
        df = pd.read_csv(PRODUTOS_CSV)
        if not df.empty:
            # Garante que a coluna 'id' seja do tipo inteiro
            df['id'] = df['id'].astype(int)
            # Atualiza o último ID com o maior ID existente no arquivo
            # *** CORREÇÃO AQUI: Converte de numpy.int64 para int nativo ***
            ultimo_id = int(df['id'].max()) 
        else:
            # Se o arquivo estiver vazio, mas existir
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
    """
    Salva o DataFrame de volta no arquivo CSV.
    Esta função DEVE ser chamada DENTRO de um 'with db_lock:'
    """
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
            
            fake = Faker('pt_BR') # Gera dados em português
            categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Ferramentas', 'Esportes', 'Livros', 'Móveis']
            novos_produtos = []
            
            # --- INÍCIO DA CORREÇÃO (Restaurando a lógica do loop) ---
            for i in range(1, 36): # 35 registros
                # Esta é a lógica correta para criar produtos falsos
                novo_produto = {
                    "id": i,
                    "nome": fake.unique.word().capitalize() + " " + fake.word(),
                    "categoria": random.choice(categorias),
                    "preco": round(random.uniform(10.5, 999.9), 2)
                }
                novos_produtos.append(novo_produto) # Adiciona à lista

            # Cria o DataFrame de novos produtos *fora* do loop
            df_novos = pd.DataFrame(novos_produtos)
            df_final = pd.concat([df, df_novos], ignore_index=True)
            
            salvar_dados(df_final)
            
            # Atualiza o ultimo_id global corretamente
            global ultimo_id
            ultimo_id = int(df_final['id'].max()) # Converte para int
            print(f"Banco de dados populado. Total de {len(df_final)} registros. Último ID: {ultimo_id}")
        else:
            print(f"Banco de dados já está populado com {len(df)} registros. Último ID: {ultimo_id}")
# --- FIM DA CORREÇÃO ---


# --- Endpoints da API (CRUD) ---

@app.post("/produtos", response_model=dict)
def cadastrar_produto(produto: Produto):
    """
    Cadastra um novo produto. Operação de escrita (usa lock).
    """
    # --- INÍCIO DA CORREÇÃO (Restaurando a lógica de adicionar um produto) ---
    with db_lock:
        df = carregar_dados()
        
        global ultimo_id
        ultimo_id += 1
        
        # Esta é a lógica correta para adicionar UM produto
        novo_produto = {
            # Garante que os tipos são nativos do Python
            "id": int(ultimo_id), 
            "nome": produto.nome,
            "categoria": produto.categoria,
            "preco": float(produto.preco)
        }
        
        df_novo = pd.DataFrame([novo_produto])
        df_final = pd.concat([df, df_novo], ignore_index=True)
        
        salvar_dados(df_final)
        
        return novo_produto
    # --- FIM DA CORREÇÃO ---

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
        
        # *** CORREÇÃO AQUI: Converte tipos Numpy para nativos antes de retornar ***
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
        
        # Retorna o produto atualizado
        # *** CORREÇÃO AQUI: Converte tipos Numpy para nativos antes de retornar ***
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

# --- Endpoints de Estatísticas (Novos Serviços) ---

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
        
        # *** CORREÇÃO AQUI: Converte tipos Numpy para nativos antes de retornar ***
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
        
        # *** CORREÇÃO AQUI: Converte tipos Numpy para nativos antes de retornar ***
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
        # *** CORREÇÃO AQUI: Converte de numpy.float64 para float nativo ***
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

# --- Para rodar a aplicação ---
# Salve como main.py e execute no terminal:
# 1. pip install fastapi uvicorn pandas faker
# 2. uvicorn main:app --reload