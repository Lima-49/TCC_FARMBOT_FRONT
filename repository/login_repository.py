import requests
import json
from config import reqUrl

class LoginRepository:
    def __init__(self) -> None:
        self.reqUrl = reqUrl
        
    def autentificar_login(self, login_obj):
        headers = {"Content-Type": "application/json"}
        
        payload = json.dumps({
            "email": login_obj.email,
            "senha": login_obj.senha
        })
        
        response = requests.request("POST", self.reqUrl+"/clientes/auth", data=payload, headers=headers, timeout=30)
        return response