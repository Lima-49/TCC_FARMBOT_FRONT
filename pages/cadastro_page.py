from models.client_model import Cliente
import style.cadastro_style as style
from script import cadastro_script as controller
import streamlit as st
from datetime import datetime

class CadastroPage:
    def __init__(self):
        self.icone_img = style.icone_img
        self.controller = controller.CadastroController()
        self.client = Cliente()
        self.datetetim_min_value = datetime.strptime("01-01-1910", "%d-%m-%Y")

    def show(self):
        st.image(self.icone_img, width=200)

        self.client.nome = st.text_input("Nome")
        self.client.sobrenome = st.text_input("Sobrenome")
        self.client.data_nascimento = st.date_input("Data de Nascimento", format='DD-MM-YYYY', value=None, min_value=self.datetetim_min_value)
        self.client.cpf = st.text_input("CPF", max_chars=11)
        self.client.email = st.text_input("E-mail")
        self.client.senha_login = st.text_input("Senha", type='password')
        self.controller.segunda_senha = st.text_input("Confirmação da Senha", type='password')
        
        if self.controller.segunda_senha:
            self.controller.validar_campos_preenchidos(self.client)

        if st.button("SALVAR", type="primary", use_container_width=True, disabled=self.controller.botao_salvar):
            self.controller.cadastrando_cliente(self.client)

        if st.button("VOLTAR PARA LOGIN", type="secondary", use_container_width=True):
            st.switch_page(r"pages\login_page.py")

cadastro = CadastroPage()
cadastro.show()