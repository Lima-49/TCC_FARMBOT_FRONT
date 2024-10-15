from repository.clients_arquivos_repository import ClientesArquivosRepository
from models.client_arquivo_model import ClientArquivos
import streamlit as st

class ConfiguracaoController:
    def __init__(self):
        self.clientes_arquivos = ClientArquivos()
        self.repository = ClientesArquivosRepository()
        self.client = st.session_state['client']
        
    def subindo_arquivo_no_bucket(self, file):
        data = self.repository.subindo_arquivo_no_bucket(self.client.client_id, file)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            st.success("Arquivo salvo com sucesso")
            return data_obj['url']
        else:
            st.toast(data_obj['error'], icon="❌")
            return None
    
    def adicionando_arquivo_por_cliente(self, clientes_arquivos):
        data = self.repository.adicionando_arquivo_por_cliente(clientes_arquivos)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 201:
            st.toast(data_obj['message'], icon="✅")
        else:
            st.toast(data_obj['message'], icon="❌")

    def obtendo_arquivos_clientes(self):
        data = self.repository.obtendo_arquivos_clientes(self.client.client_id)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            self.clientes_arquivos = data_obj
            st.session_state['clientes_arquivos'] = self.clientes_arquivos
        else:
            self.clientes_arquivos = None