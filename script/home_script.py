from repository.clients_arquivos_repository import ClientesArquivosRepository
from models.client_arquivo_model import ClientArquivos
import streamlit as st

class HomeController:
    def __init__(self):
        self.clientes_arquivos_repository = ClientesArquivosRepository()
        self.clientes_arquivos = ClientArquivos()
        self.client = st.session_state['client']
        
    def obtendo_arquivos_clientes(self):
        id_cliente = self.client.id_client
        data = self.clientes_arquivos_repository.obtendo_arquivos_clientes(id_cliente)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 404:
            self.clientes_arquivos = None
        else:
            self.clientes_arquivos = [self.clientes_arquivos.from_dict(item) for item in data_obj]
        
        