from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()
   
# Modelo de dados
class Usuario(BaseModel):
    cpf: int
    nome: str
    data_nascimento: date

# Lista de usuários
users = []

# Rota raiz
@app.get("/")
def read_root():
    return {"Documentation": "/docs", "GET": "/users", "GET": "/users?cpf={cpf}", "POST": "/user"}

# GET usuários
@app.get("/users")
def read_user(cpf: int | None = None):
    if cpf:
        for user in users:
            if user.cpf == cpf:
                return user
        return {"Erro": "Usuário não encontrado"}
    return users

# POST usuário
@app.post("/user")
def create_user(user: Usuario):
    users.append(user)
    return user
