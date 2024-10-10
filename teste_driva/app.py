import streamlit as st
import plotly.express as px
from etl import MarketData

etl = MarketData('data/Cópia de Teste visualização de dados.xlsx')
etl.load_sales()
etl.load_products()
# etl.best_selling_days()
# etl.daily_sales()
# etl.sales_per_product()
etl.best_banana_selling_day()

st.title('Teste Driva - Análise de vendas na Feira')

st.header('Evolução do faturamento ao longo do tempo')
daily_sales = etl.con.execute("SELECT 42")

if __name__ == '__main__':
    pass