from script.home_script import HomeController
import pandas as pd
import streamlit as st

class HomePage:
    def __init__(self):
        self.controller = HomeController()
        
    def show(self):
        st.title("Página Principal")

        if self.controller.clientes_arquivos is None:
            st.warning("Você ainda não possui nenhum arquivo configurado na sua conta.")
            
            # Botão para redirecionar o usuário para a página de configuração
            if st.button("Ir para a página de configuração"):
                st.switch_page(r"pages\configuracao_page.py")  # Nome da página de configuração

        else:
            # Título da página
            st.title("Painel Gerencial - Informações do Estabelecimento")

            # Visão Geral
            st.header("Visão Geral")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total de Clientes", len(self.controller.clientes_df))
            col2.metric("Total de Fornecedores", len(self.controller.fornecedores_df))
            col3.metric("Total de Produtos no Estoque", self.controller.estoque_df["QUANTIDADE"].sum())
            col4.metric("Média de Produtos por Fornecedor", f"{self.controller.estoque_df['QUANTIDADE'].mean():.2f}")

            # Estatísticas
            st.header("Estatísticas")

            # Top 5 Produtos com Maior Estoque
            st.subheader("Top 5 Produtos com Maior Estoque")
            top_produtos = self.controller.estoque_df.nlargest(5, "QUANTIDADE")
            st.table(top_produtos[["PRODUTO", "QUANTIDADE"]])
            
            # Conversão da data para o tipo datetime
            self.controller.vendas_df['DATA VENDA'] = pd.to_datetime(self.controller.vendas_df['DATA VENDA'])

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Faturamento Mensal")
                self.controller.vendas_df['MÊS'] = self.controller.vendas_df['DATA VENDA'].dt.to_period('M')
                faturamento_mensal = self.controller.vendas_df.groupby('MÊS')['VALOR TOTAL'].sum()
                st.line_chart(faturamento_mensal)

            with col2:
                st.subheader("Top 10 Produtos Mais Vendidos")
                produtos_mais_vendidos = self.controller.vendas_df.groupby('PRODUTO COMPRADO')['QUANTIDADE PRODUTO'].sum().nlargest(10)
                st.bar_chart(produtos_mais_vendidos)


            col3, col4 = st.columns(2)
            with col3:
                # Clientes que Mais Compraram
                st.subheader("Top 10 Clientes - Maior Faturamento")
                clientes_top = self.controller.vendas_df.groupby('NOME CLIENTE')['VALOR TOTAL'].sum().nlargest(10)
                st.bar_chart(clientes_top)

            with col4:
                # Receita por Produto
                st.subheader("Receita por Produto")
                receita_por_produto = self.controller.vendas_df.groupby('PRODUTO COMPRADO')['VALOR TOTAL'].sum().sort_values(ascending=False)
                st.bar_chart(receita_por_produto)


# Instancia e exibe a HomePage
home = HomePage()
home.show()
