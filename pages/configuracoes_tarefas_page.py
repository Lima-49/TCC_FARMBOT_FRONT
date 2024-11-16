import streamlit as st
from script.configuracoes_tarefas_script import ConfiguracoesTarefasController
from models.configuracoes_tarefas_model import ConfiguracaoTarefaModel

class ConfiguracoesTarefas:
    def __init__(self) -> None:
        self.config_tarefa_model = ConfiguracaoTarefaModel()
        self.controller = ConfiguracoesTarefasController()
    
    def config_orcamentos(self):
        
        ativo = True if self.controller.return_value_or_default('fl_ativo', False) == 1 else False
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço",
                                                        key='orcamento_ativo',
                                                        value=ativo)
        if self.config_tarefa_model.fl_ativo:

            self.config_tarefa_model.tipo_tarefa = 0
            
            self.config_tarefa_model.produto_descr = st.selectbox(
                "Selecione um produto",
                ("remedio_1", "remedio_2", "remedio_3"),
                index=None,
                placeholder="Produtos",
                key='orcamento_produto'
            )

            self.config_tarefa_model.fornecedor_descr = st.selectbox(
                "Selecione o fornecedor desse produto",
                ("fornecedor_1", "fornecedor_2", "fornecedor_3"),
                index=None,
                placeholder="Fornecedores",
                key='orcamento_fornecedor'
            )
            
            self.config_tarefa_model.qtd_minina = st.text_input(
                'Quantidade minima de estoque do produto', 
                key='orcamento_qtd_minima'
            )
            
            self.config_tarefa_model.fl_execucao = st.radio(
                "Qual o perído de execução",
                ["Imediato", "Uma vez por dia", "Uma vez por semana", "Uma vez por mês"],
                help="Independente da opção selecionada, o horário de execução é no final do dia",
                key='orcamento_execucao'
            )
            
            st.button("SALVAR", use_container_width=True, key='orcamento_salvar')

    def config_notificacoes_clientes(self):
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço", key='notificacao_ativo')
        
        if self.config_tarefa_model.fl_ativo:
            
            self.config_tarefa_model.tipo_tarefa = 1
            
            self.config_tarefa_model.produto_desc = st.selectbox(
                "Selecione um produto",
                ("remedio_1", "remedio_2", "remedio_3"),
                index=None,
                placeholder="Produtos",
                key='notificacao_produto'
            )
            
            self.config_tarefa_model.oferta_desc = st.text_area(
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
            
            st.button("SALVAR", use_container_width=True, key='notificacao_salvar')
        
    def config_produtos_campanhas(self):
        self.config_tarefa_model.fl_ativo = st.checkbox("Ativar o serviço", key='produto_ativo')
        
        if self.config_tarefa_model.fl_ativo:

            self.config_tarefa_model.tipo_tarefa = 2
            
            self.config_tarefa_model.fl_execucao = st.radio(
                "Qual o perído de execução",
                ["Imediato", "Uma vez por dia", "Uma vez por semana", "Uma vez por mês"],
                help="Independente da opção selecionada, o horário de execução é no final do dia",
                key='produto_execucao'
            )
            
            st.button("SALVAR", use_container_width=True, key='produto_salvar')

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
