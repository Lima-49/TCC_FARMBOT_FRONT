from script.home_script import HomeController
import streamlit as st

class HomePage:
    def __init__(self):
        self.controller = HomeController()
        self.controller.obtendo_arquivos_clientes()
        
    def show(self):
        st.title("Página Principal")

        if self.controller.clientes_arquivos is None:
            st.warning("Você ainda não possui nenhum arquivo configurado na sua conta.")
            
            # Botão para redirecionar o usuário para a página de configuração
            if st.button("Ir para a página de configuração"):
                st.switch_page(r"pages\configuracao_page.py")  # Nome da página de configuração

        else:
            st.subheader("Seus Gráficos")
            # Exibe os gráficos baseados nos dados do cliente
            # Aqui você pode inserir gráficos usando bibliotecas como matplotlib ou plotly
            st.line_chart(self.controller.clientes_arquivos)  # Exemplo com gráfico genérico

# Instancia e exibe a HomePage
home = HomePage()
home.show()
