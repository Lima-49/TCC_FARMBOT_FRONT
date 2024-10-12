from repository.clients_arquivos_repository import ClientesArquivosRepository
from models.client_arquivo_model import ClientArquivos
import streamlit as st

class HomeController:
    def __init__(self):
        self.clientes_arquivos_repository = ClientesArquivosRepository()
        self.clientes_arquivos = ClientArquivos()
        self.client = st.session_state['client']
        
    def obtendo_arquivos_clientes(self):
        id_cliente = self.client.client_id
        data = self.clientes_arquivos_repository.obtendo_arquivos_clientes(id_cliente)
        
        if data:
            if data.response_code == 404:
                st.toast(data.message, icon="❌")
            else:
                self.clientes_arquivos = self.clientes_arquivos.from_dict(data)
        
        