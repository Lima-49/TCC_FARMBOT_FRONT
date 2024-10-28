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
        st.write('#')
        with st.container(border=True):
            _, c, _ = st.columns(3, vertical_alignment='top')
            with c:
                st.write('')
                st.image(self.icone_img, width=200)
                st.write('##')

            _, c2, _ = st.columns([0.1, 0.8, 0.1], vertical_alignment="top")

            with c2:
                b1, b2 = st.columns(2)

                with b1:
                    self.client.nome = st.text_input("Nome")
                    self.client.data_nascimento = st.date_input(
                        "Data de Nascimento", format='DD-MM-YYYY',
                        value=None, min_value=self.datetetim_min_value
                    )

                with b2:
                    self.client.sobrenome = st.text_input("Sobrenome")
                    self.client.cpf = st.text_input("CPF/CNPJ", max_chars=12)

                self.client.email = st.text_input("E-mail")

                b3, b4 = st.columns(2)

                with b3:
                    self.client.senha_login = st.text_input(
                        "Senha", type='password'
                    )

                with b4:
                    self.controller.segunda_senha = st.text_input(
                        "Confirmação da Senha", type='password'
                    )

                if self.controller.segunda_senha:
                    self.controller.validar_campos_preenchidos(self.client)

                if st.button("SALVAR", type="primary", use_container_width=True,
                             disabled=self.controller.botao_salvar):
                    self.controller.cadastrando_cliente(self.client)

                if st.button("VOLTAR PARA LOGIN", type="secondary",
                             use_container_width=True):
                    st.switch_page(r"pages\login_page.py")

            st.markdown('</div>', unsafe_allow_html=True)


cadastro = CadastroPage()
cadastro.show()