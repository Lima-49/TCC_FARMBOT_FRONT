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
        col1, col2 = st.columns(2)

        with col1:
            st.image(self.background_img, use_column_width=True)

        with col2:
            st.image(self.icone_img, width=200)

            self.login.email = st.text_input("E-mail *")
            self.login.senha = st.text_input("Senha *", type="password")

            if st.button("ENTRAR", type="primary", use_container_width=True):
                self.controller.autentificar_login(self.login)

            if st.button("CADASTRAR", type="secondary", use_container_width=True):
                st.switch_page(r"pages\cadastro_page.py")
                
login = LoginPage()
login.show()