import requests
import json

class LoginRepository:
    def __init__(self) -> None:
        self.reqUrl = "http://127.0.0.1:5000"
        
    def autentificar_login(self, client_email):
        headers = {"Content-Type": "application/json"}
        response = requests.request("GET", self.reqUrl+f"/clientes/{client_email}", headers=headers, timeout=30)
        return response.json()