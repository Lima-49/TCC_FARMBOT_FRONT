# from app.app import apiUrl
import requests
import json

class CadastroRepository:
    def __init__(self) -> None:
        self.reqUrl = "http://127.0.0.1:5000"
    
    def cadastro_aluno(self, client):
        
        # Certifique-se de passar o cabeçalho com o content-type JSON
        headers = {"Content-Type": "application/json"}
        
        payload = json.dumps({
            "cpf": client.cpf,
            "data_nascimento": client.data_nascimento.strftime("%d-%m-%Y"),
            "email": client.email,
            "nome": client.nome,
            "sobrenome": client.sobrenome,
            "senha_login": client.senha_login
        })
        
        response = requests.request("POST", self.reqUrl+"/clientes", data=payload, headers=headers, timeout=30)
        
        return response