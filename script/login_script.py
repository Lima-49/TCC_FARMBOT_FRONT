from repository.login_repository import LoginRepository
from models.client_model import Cliente
import streamlit as st
import bcrypt

class LoginController:
    def __init__(self):
        self.repository = LoginRepository()
        self.client = Cliente()
        
    def autentificar_login(self, login_obj):
        client_email = login_obj.email
        data = self.repository.autentificar_login(client_email)
        
        if data:
            self.client = self.client.from_dict(data)
            
            valida_senha = self.verificar_senha(login_obj.senha, self.client.senha_login)
            if valida_senha:
                st.switch_page(r'pages\home.py')
            else:
                st.toast("E-mail ou senha incorretos", icon="❌")
        else:
            st.toast(data, icon="❌")

    def verificar_senha(self, senha_fornecida, senha_hashed):
        # Verifica se a senha fornecida corresponde ao hash
        return bcrypt.checkpw(senha_fornecida.encode('utf-8'), senha_hashed.encode('utf-8'))