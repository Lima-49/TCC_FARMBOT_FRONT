from repository.configuracoes_tarefas_repository import ConfiguracoesTarefasRepository
from models.configuracoes_tarefas_model import ConfiguracaoTarefaModel
import streamlit as st

class ConfiguracoesTarefasController:
    def __init__(self):
        self.client = st.session_state['client']
        self.arquivos = st.session_state['clientes_arquivos']
        self.repo = ConfiguracoesTarefasRepository()
        self.config_tarefas_model = ConfiguracaoTarefaModel()
        self.config_tarefas = self.buscar_configuracoes_por_clientes()
    
    def return_value_or_default(self, field, default_value):
        return self.config_tarefas[field] if self.config_tarefas is not None else default_value

    def buscar_configuracoes_por_clientes(self):
        data = self.repo.obtendo_configuracoes_por_cliente(self.client.id_client)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            config_tarefas = [self.config_tarefas_model.from_dict(item) for item in data_obj]
        else:
            config_tarefas = None
            
        return config_tarefas
            