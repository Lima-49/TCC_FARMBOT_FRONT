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
            "tipo_arquivo": cliente_arquivo.tipo_arquivo,
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
    
    def removendo_arquivo_do_bucket(self, id_arquivo):
        headers = {"Content-Type": "application/json"}
        reponse = requests.request('DELETE', self.reqUrl+f'/files/{id_arquivo}', headers=headers, timeout=30)
        return reponse
    
    def baixando_arquivos_do_bucket(self, id_client, tipo_arquivo):
        headers = {"Content-Type": "application/json"}
        response = requests.request('GET', self.reqUrl+f'/files/download_file/{id_client}/{tipo_arquivo}',
                                    headers=headers,
                                    timeout=30)
        return response