import requests
from config import reqUrl
import json

class ClientesArquivosRepository:
    def __init__(self):
        self.reqUrl = reqUrl
        
    def adicionando_arquivo_por_cliente(self, cliente_arquivo):
        headers = {"Content-Type": "application/json"}
        
        payload = json.dumps({
            "id_cliente": cliente_arquivo.id_cliente,
            "descricao_arquivo": cliente_arquivo.descricao_arquivo,
            "url_bucket": cliente_arquivo.url_bucket,
            "nome_arquivo": cliente_arquivo.nome_arquivo
        })
        
        response = requests.request("POST", self.reqUrl+"/files", data=payload, headers=headers, timeout=30)
        
        return response
    
    def subindo_arquivo_no_bucket(self, id_client, files):
        response = requests.request('POST', self.reqUrl+f"/files/{str(id_client)}/upload-file", files=files, timeout=30)
        
        return response
    
    def obtendo_arquivos_clientes(self, id_client):
        headers = {"Content-Type": "application/json"}
        
        response = requests.request("GET", self.reqUrl+f"/files/{str(id_client)}/files", headers=headers, timeout=30)
        
        return response