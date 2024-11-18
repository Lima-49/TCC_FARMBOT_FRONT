import streamlit as st
from script.configuracoes_tarefas_script import ConfiguracoesTarefasController
from models.configuracoes_tarefas_model import ConfiguracaoTarefaModel
class ConfiguracoesTarefas:
    def __init__(self) -> None:
        self.config_tarefa_model = ConfiguracaoTarefaModel()
        self.controller = ConfiguracoesTarefasController()
    
    @st.dialog("Nova Configuração")
    def config_orcamento_form(self):
        self.config_tarefa_model.tipo_tarefa = 0
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço",
                                                        key='orcamento_ativo')
        if self.config_tarefa_model.fl_ativo:
            
            self.config_tarefa_model.produto_descr = st.selectbox(
                "Selecione um produto",
                self.controller.lista_produtos,
                placeholder="Produtos",
                key='orcamento_produto',
            )

            self.config_tarefa_model.fornecedor_descr = st.selectbox(
                "Selecione o fornecedor desse produto",
                self.controller.lista_fornecedores,
                index=None,
                placeholder="Fornecedores",
                key='orcamento_fornecedor'
            )
                        
            self.config_tarefa_model.qtd_minima = st.text_input(
                'Quantidade minima de estoque do produto', 
                key='orcamento_qtd_minima'
            )
            
            self.config_tarefa_model.fl_execucao = st.radio(
                "Qual o perído de execução",
                ["Imediato", "Uma vez por dia", "Uma vez por semana", "Uma vez por mês"],
                help="Independente da opção selecionada, o horário de execução é no final do dia",
                key='orcamento_execucao'
            )
            
            if st.button("SALVAR", use_container_width=True, key='orcamento_salvar'):
                with st.spinner("Salvando configuração..."):
                    self.controller.salvar_configuracao(self.config_tarefa_model)
                    st.session_state['configs_tarefas'] = self.config_tarefa_model
                st.rerun()

    @st.dialog("Nova Configuração")
    def config_notificacao_cliente_form(self):
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço", key='notificacao_ativo')
        self.config_tarefa_model.tipo_tarefa = 1
        if self.config_tarefa_model.fl_ativo:
            
            self.config_tarefa_model.produto_descr = st.selectbox(
                "Selecione um produto",
                self.controller.lista_produtos,
                index=None,
                placeholder="Produtos",
                key='notificacao_produto'
            )
            
            self.config_tarefa_model.oferta_descr = st.text_area(
                'Descrição da Oferta', 
                help="Escreva uma breve mensagem informando o tipo de oferta que está sendo oferecida",
                key='notificacao_oferta_desc'
            )
            
            self.config_tarefa_model.fl_execucao = st.radio(
                "Qual o perído de execução",
                ["Imediato", "Uma vez por dia", "Uma vez por semana", "Uma vez por mês"],
                help="Independente da opção selecionada, o horário de execução é no final do dia",
                key='notificacao_execucao'
            )
            
            if st.button("SALVAR", use_container_width=True, key='notificacao_salvar'):
                with st.spinner("Salvando configuração..."):
                    self.controller.salvar_configuracao(self.config_tarefa_model)
                    st.session_state['configs_tarefas'] = self.config_tarefa_model
                st.rerun()

    @st.dialog("Nova Configuração")
    def config_produtos_campanhas_form(self):    
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço", key='produto_ativo')
        self.config_tarefa_model.tipo_tarefa = 2
        if self.config_tarefa_model.fl_ativo:
            
            self.config_tarefa_model.fl_execucao = st.radio(
                "Qual o perído de execução",
                ["Imediato", "Uma vez por dia", "Uma vez por semana", "Uma vez por mês"],
                help="Independente da opção selecionada, o horário de execução é no final do dia",
                key='produto_execucao'
            )
            
            if st.button("SALVAR", use_container_width=True, key='produto_salvar'):
                with st.spinner("Salvando configuração..."):
                    self.controller.salvar_configuracao(self.config_tarefa_model)
                    st.session_state['configs_tarefas'] = self.config_tarefa_model
                st.rerun()
            
    def config_orcamentos(self):
        
        self.config_tarefa_model.tipo_tarefa = 0
        
        if st.button("Adicionar nova configuração", key='btn_config_orcamento'):
            self.config_orcamento_form()

        if st.session_state['configs_tarefas'] is not None:
            df = self.controller.create_config_table_visualizatio(st.session_state['configs_tarefas'], self.config_tarefa_model.tipo_tarefa)
            if not df.empty:
                st.data_editor(df, num_rows="fixed", key='table_config_orcamento')
            
    def config_notificacoes_clientes(self):
        self.config_tarefa_model.tipo_tarefa = 1
        
        if st.button("Adicionar nova configuração", key='btn_config_notificaca'):
            self.config_notificacao_cliente_form()

        if st.session_state['configs_tarefas'] is not None:
            df = self.controller.create_config_table_visualizatio(st.session_state['configs_tarefas'], self.config_tarefa_model.tipo_tarefa)
            if not df.empty:
                st.data_editor(df, num_rows="fixed", key='table_config_notificacao')
        
    def config_produtos_campanhas(self):

        self.config_tarefa_model.tipo_tarefa = 2
            
        if st.button("Adicionar nova configuração", key='btn_config_produtos_campanhs'):
            self.config_produtos_campanhas_form()
            
        if st.session_state['configs_tarefas'] is not None:
            df = self.controller.create_config_table_visualizatio(st.session_state['configs_tarefas'],self.config_tarefa_model.tipo_tarefa)
            if not df.empty:
                st.data_editor(df, num_rows="fixed", key='table_config_produtos')
                
    def show(self):
        st.title("Configurações das Tarefas")
        
        if self.controller.arquivos is None or len(self.controller.arquivos)<3:
            st.warning("Você ainda não possui todos os arquivos configurado na sua conta. Por favor configure os 3 principais arquivos na página de configuração")
            
            if st.button("Ir para a página de configuração"):
                st.switch_page(r"pages\configuracao_page.py")
        else:
            tab_orcamentos, tab_noti_clientes, tab_produtos_campanhas = st.tabs([
                'Orçamento Automatizado', 
                'Ofertas para clientes', 
                'Produtos para Campanhas'
            ])
            
            with tab_orcamentos:
                self.config_orcamentos()
                
            with tab_noti_clientes:
                self.config_notificacoes_clientes()
                
            with tab_produtos_campanhas:
                self.config_produtos_campanhas()
            
if __name__ == '__main__':
    config = ConfiguracoesTarefas()
    config.show()
