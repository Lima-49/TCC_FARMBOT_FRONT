import streamlit as st
import style.login_style as style
from models.login_model import Login
from script.login_script import LoginController


class LoginPage:
    def __init__(self):
        self.background_img = style.background_img
        self.icone_img = style.icone_img
        self.login = Login()
        self.controller = LoginController()

    def show(self):
        st.write('#')
        with st.container(border=True):
            st.write('')
            _, c, _ = st.columns(3, vertical_alignment='center')
            with c:
                st.image(self.icone_img, width=200)
                st.write('##')

            _, c2, _ = st.columns([0.1, 0.8, 0.1], vertical_alignment="top")

            with c2:
                self.login.email = st.text_input("E-mail *")
                self.login.senha = st.text_input(
                    "Senha *", type="password", autocomplete='current-password')

                st.write('###')

                b1, b2 = st.columns(2)
                with b1:
                    if st.button("ENTRAR", type="primary", use_container_width=True):
                        self.controller.autentificar_login(self.login)

                with b2:
                    if st.button("CADASTRAR", type="secondary", use_container_width=True):
                        st.switch_page(r"pages\cadastro_page.py")

                st.write('')


login = LoginPage()
login.show()