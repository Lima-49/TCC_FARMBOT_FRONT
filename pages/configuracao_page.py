import streamlit as st
from script.configuracao_script import ConfiguracaoController
from models.client_arquivo_model import ClientArquivos

class ConfiguracaoPage:
    def __init__(self):
        self.controller = ConfiguracaoController()
        self.clientes_arquivos_model = ClientArquivos()
        self.controller.obtendo_arquivos_clientes()
    
    @st.dialog("Upload de Arquivos")
    def upload_file(self, file):
        self.clientes_arquivos_model.id_cliente = self.controller.client.id_client
        self.clientes_arquivos_model.nome_arquivo = st.text_input("Nome do arquivo", value=file['file'][0])
        self.clientes_arquivos_model.descricao_arquivo = st.text_area("Descrição do arquivo")
        
        if st.button("SALVAR", type='primary', use_container_width=True):
            with st.spinner('Enviando arquivo...'):
                url_file = self.controller.subindo_arquivo_no_bucket(file)
                if url_file is not None:
                    self.clientes_arquivos_model.url_bucket = url_file
                    self.controller.adicionando_arquivo_por_cliente(self.clientes_arquivos_model)
                    st.session_state['clientes_arquivos'] = self.clientes_arquivos_model
                else:
                    st.toast("Erro ao salvar o arquivo", icon="❌")
            st.rerun()

    def show(self):
        # Título da página
        st.title('Upload de Arquivos')

        # Criar o componente de upload
        uploaded_file = st.file_uploader("Escolha um arquivo (CSV ou Excel)", type=['csv', 'xlsx'])

        # Verificar se o arquivo foi enviado
        if uploaded_file is not None:
            # Exibir nome do arquivo
            st.write(f"Arquivo {uploaded_file.name} carregado com sucesso!")

            # Converter o arquivo para ser enviado via requests
            files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
            
            self.upload_file(files)
            
        if "clientes_arquivos" in st.session_state:
            df = self.controller.ajustando_tabela_de_dados()
            st.data_editor(df, use_container_width=True, num_rows="fixed")

config = ConfiguracaoPage()
config.show()
