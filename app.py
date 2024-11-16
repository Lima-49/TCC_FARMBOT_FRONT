import streamlit as st

# Configurações da página (primeira função Streamlit chamada)
st.set_page_config(page_title="FarmBot", page_icon=r"assets/ico.ico", initial_sidebar_state="collapsed")

st.session_state['client'] = None
st.session_state['clientes_arquivos'] = None
st.session_state['config_tarefas'] = None

# Navegando para a pagina de login
st.switch_page(r"pages\login_page.py")
