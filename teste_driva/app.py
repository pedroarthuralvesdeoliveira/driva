import streamlit as st
import plotly.express as px
from etl import MarketData

etl = MarketData('data/Cópia de Teste visualização de dados.xlsx')
etl.load_sales()
etl.load_products()

st.title('Teste Driva - Análise de vendas na Feira')

if __name__ == '__main__':
    pass