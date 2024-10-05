from repository.cadastro_respository import CadastroRepository
import streamlit as st

class CadastroController:
    def __init__(self):
        self.repository = CadastroRepository()
        self.botao_salvar = True
        self.segunda_senha = None
        
    def cadastrando_cliente(self, client):
        data = self.repository.cadastro_aluno(client)
        if data:
            st.toast("Cadastro realizado com sucesso!", icon="✅")
            
    def validar_campos_preenchidos(self, clientes_campos):
        if not all([clientes_campos.nome, clientes_campos.sobrenome, clientes_campos.data_nascimento, clientes_campos.cpf, clientes_campos.email, clientes_campos.senha_login]):
            st.toast("Todos os campos precisam ser preenchidos", icon="❌")
        if clientes_campos.senha_login != self.segunda_senha:
            st.toast("Senhas não conferem", icon="❌")
        else:
            self.botao_salvar = False