from repository.login_repository import LoginRepository
from models.client_model import Cliente
import streamlit as st

class LoginController:
    def __init__(self):
        self.repository = LoginRepository()
        self.client = Cliente()

    def autentificar_login(self, login_obj):
        data = self.repository.autentificar_login(login_obj)
        status_code = data.status_code
        data_obj = data.json()
        
        if status_code == 200:
            self.client = self.client.from_dict(data_obj)
            
            if self.client:
                st.session_state['client'] = self.client
                st.switch_page(r'pages\home_page.py')
        else:
            st.toast(data_obj['message'], icon="❌")

