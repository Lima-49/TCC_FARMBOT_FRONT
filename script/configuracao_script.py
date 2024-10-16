from repository.clients_arquivos_repository import ClientesArquivosRepository
from models.client_arquivo_model import ClientArquivos
import streamlit as st
import pandas as pd

class ConfiguracaoController:
    def __init__(self):
        self.clientes_arquivos = ClientArquivos()
        self.repository = ClientesArquivosRepository()
        self.client = st.session_state['client']
        
    def subindo_arquivo_no_bucket(self, file):
        data = self.repository.subindo_arquivo_no_bucket(self.client.id_client, file)
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
        data = self.repository.obtendo_arquivos_clientes(self.client.id_client)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            self.clientes_arquivos = data_obj
            st.session_state['clientes_arquivos'] = self.clientes_arquivos
        else:
            self.clientes_arquivos = None
            
    def ajustando_tabela_de_dados(self):
        df = pd.DataFrame(self.clientes_arquivos)
        df = df.rename(columns={'nome_arquivo':'Nome do Arquivo', 'descricao_arquivo':"Descrição do Arquivo", 'id_arquivo':'ID'})
        df.index = df['ID']
        df = df[['Nome do Arquivo','Descrição do Arquivo']]
        return df

    def removendo_arquivo_do_bucket(self, id_arquivo):
        data = self.repository.removendo_arquivo_do_bucket(id_arquivo)
        status_code = data.status_code
        data_obj = data.json()
        st.toast(data_obj['message'], icon="✅" if status_code == 200 else "❌")