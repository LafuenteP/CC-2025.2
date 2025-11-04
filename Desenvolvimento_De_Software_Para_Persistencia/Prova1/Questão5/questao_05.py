from bs4 import BeautifulSoup

def verificar_vitoria_j1(jogada1: str, jogada2: str) -> bool:
    """Verifica se o Jogador 1 venceu o Jogador 2."""
    
    j1 = jogada1.strip().lower()
    j2 = jogada2.strip().lower()

    if j1 == j2:
        return False

    if (j1 == "pedra" and j2 == "tesoura") or \
       (j1 == "tesoura" and j2 == "papel") or \
       (j1 == "papel" and j2 == "pedra"):
        return True
    
    return False

vitorias_jogador_1 = 0

try:
    with open("questao_05.html", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    corpo_tabela = soup.find("tbody")

    if corpo_tabela:
        linhas_jogadas = corpo_tabela.find_all("tr")
        
        for linha in linhas_jogadas:
            
            celulas = linha.find_all("td")
            jogada_j1 = celulas[0].get_text()
            jogada_j2 = celulas[1].get_text()
            if verificar_vitoria_j1(jogada_j1, jogada_j2):
                vitorias_jogador_1 += 1
                # print(f"DEBUG: J1 venceu ({jogada_j1.strip()} vs {jogada_j2.strip()})")

    print(f"O Jogador 1 venceu {vitorias_jogador_1} vez(es).")

except FileNotFoundError:
    print("Erro: O arquivo 'jogadas.html' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")