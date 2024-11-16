from repository.configuracoes_tarefas_repository import ConfiguracoesTarefasRepository
from models.configuracoes_tarefas_model import ConfiguracaoTarefaModel
import streamlit as st
import pandas as pd

class ConfiguracoesTarefasController:
    def __init__(self):
        self.client = st.session_state['client']
        self.arquivos = st.session_state['clientes_arquivos']
        self.repo = ConfiguracoesTarefasRepository()
        self.config_tarefas_model = ConfiguracaoTarefaModel()
        self.config_tarefas = self.buscar_configuracoes_por_clientes()
        self.lista_fornecedores = self.obtendo_lista('1', 'EMPRESA')
        self.lista_produtos = self.obtendo_lista('2', 'PRODUTO COMPRADO')
    
    def return_value_or_default(self, field, default_value):
        return self.config_tarefas[field] if self.config_tarefas is not None else default_value

    def buscar_configuracoes_por_clientes(self):
        data = self.repo.obtendo_configuracoes_por_cliente(self.client.id_client)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            config_tarefas = [self.config_tarefas_model.from_dict(item) for item in data_obj]
            st.session_state['configs_tarefas'] = config_tarefas
        else:
            config_tarefas = None
            
        return config_tarefas
            
    def salvar_configuracao(self, config_tarefa):
        
        if config_tarefa.fl_execucao == 'Imediato':
            config_tarefa.fl_execucao = 0
        elif config_tarefa.fl_execucao == 'Uma vez por dia':
            config_tarefa.fl_execucao = 1
        elif config_tarefa.fl_execucao == 'Uma vez por semana':
            config_tarefa.fl_execucao = 2
        elif config_tarefa.fl_execucao == 'Uma vez por mês':
            config_tarefa.fl_execucao = 3
        
        config_tarefa.fl_ativo = 1 if config_tarefa.fl_ativo else 0
        config_tarefa.qtd_minima = int(config_tarefa.qtd_minima) if config_tarefa.qtd_minima is not None else 0
            
        config_tarefa.id_cliente = self.client.id_client
        
        data = self.repo.adicionando_nova_configuracao(config_tarefa)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 201:
            st.toast(data_obj['message'], icon="✅")
        else:
            st.toast(data_obj['message'], icon="❌")
            
    def create_config_table_visualizatio(self, data, tipo_tarefa):
        
        objetos_filtrados = filter(lambda obj: obj.tipo_tarefa == tipo_tarefa, data)
        df_list = []

        for item in objetos_filtrados:
            item = self.config_tarefas_model.to_dict(item)
            df = pd.DataFrame(item, index=[0])
            df_list.append(df)

        if len(df_list)>0:
            df_final = pd.concat(df_list).reset_index(drop=True)
            return df_final
        else:
            return pd.DataFrame()
          
    def obtendo_lista(self, tipo_arquivo, coluna_lista):
        data = self.repo.obtendo_lista_de_fornecedores(self.client.id_client, tipo_arquivo, coluna_lista)
        status_code = data.status_code
        
        if status_code == 200:
            data_obj = data.json()
            return data_obj
        else:
            return []
            
    
