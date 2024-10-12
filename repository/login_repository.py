import requests
from config import reqUrl
class LoginRepository:
    def __init__(self) -> None:
        self.reqUrl = reqUrl
        
    def autentificar_login(self, client_email):
        headers = {"Content-Type": "application/json"}
        response = requests.request("GET", self.reqUrl+f"/clientes/{client_email}", headers=headers, timeout=30)
        return response.json()