from repository.clients_arquivos_repository import ClientesArquivosRepository
from models.client_arquivo_model import ClientArquivos
import pandas as pd
import streamlit as st

class HomeController:
    def __init__(self):
        self.clientes_arquivos_repository = ClientesArquivosRepository()
        self.clientes_arquivos = ClientArquivos()
        self.client = st.session_state['client']
        self.obtendo_arquivos_clientes()
        self.init_files()
        
    def init_files(self):
        if st.session_state['clientes_arquivos'] is not None:
            self.clientes_df = self.baixando_arquivos_do_bucket(0)
            self.fornecedores_df = self.baixando_arquivos_do_bucket(1)
            self.vendas_df = self.baixando_arquivos_do_bucket(2)
            self.estoque_df = self.baixando_arquivos_do_bucket(3)
        
    def obtendo_arquivos_clientes(self):
        id_cliente = self.client.id_client
        data = self.clientes_arquivos_repository.obtendo_arquivos_clientes(id_cliente)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 404:
            self.clientes_arquivos = None
        else:
            self.clientes_arquivos = [self.clientes_arquivos.from_dict(item) for item in data_obj]
            
        st.session_state['clientes_arquivos'] = self.clientes_arquivos
        
    def baixando_arquivos_do_bucket(self, tipo_arquivo):
        id_cliente = self.client.id_client
        data = self.clientes_arquivos_repository.baixando_arquivos_do_bucket(id_cliente, tipo_arquivo)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            df = pd.DataFrame(data_obj)
            return df
        else:
            return pd.DataFrame()