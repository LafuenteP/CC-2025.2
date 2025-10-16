import httpx

BASE_URL = "http://127.0.0.1:8000"

def criar_Aluno():
    response = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"Nome": "Nicolas", "Curso": "CC", "IRA": 10}
    )
    print(response.json()["MSG"])
    print(response.json()["Aluno"])

criar_Aluno()