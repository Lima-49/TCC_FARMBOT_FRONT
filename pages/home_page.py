from script.home_script import HomeController
import streamlit as st

class HomePage:
    def __init__(self):
        self.controller = HomeController()
        
    def show(self):
        st.title("GRAFICOS")
        teste = self.controller.obtendo_arquivos_clientes()
        

home = HomePage()
home.show()

