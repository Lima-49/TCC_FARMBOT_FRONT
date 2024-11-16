import requests
from config import reqUrl
import json

class ConfiguracoesTarefasRepository:
    def __init__(self):
        self.reqUrl = reqUrl
        
    def adicionando_nova_configuracao(self, configuracao_tarefa):
        headers = {"Content-Type": "application/json"}
        
        payload = json.dumps({
            "id_cliente": configuracao_tarefa.id_cliente,
            "tipo_tarefa": configuracao_tarefa.tipo_tarefa,
            "produto_descr": configuracao_tarefa.produto_descr,
            "fornecedor_descr": configuracao_tarefa.fornecedor_descr,
            "qtd_minima": configuracao_tarefa.qtd_minima,
            "oferta_descr": configuracao_tarefa.oferta_descr,
            "fl_ativo": configuracao_tarefa.fl_ativo,
            "fl_execucao":configuracao_tarefa.fl_execucao
        })
        
        response = requests.request("POST", self.reqUrl+'/configuracao-tarefa', data=payload, headers=headers, timeout=30)
        return response
    
    def obtendo_configuracoes_por_cliente(self, id_cliente):
        headers = {"Content-Type": "application/json"}
        response = requests.request('GET', self.reqUrl+f'/configuracao-tarefa/{id_cliente}', headers=headers, timeout=30)
        return response

    def obtendo_lista_de_fornecedores(self, id_cliente, tipo_arquivo, coluna_lista):
        headers = {"Content-Type": "application/json"}
        response = requests.request('GET', self.reqUrl+f'/configuracao-tarefa/lista-fornecedores/{id_cliente}/{tipo_arquivo}/{coluna_lista}', headers=headers, timeout=30)
        return response              