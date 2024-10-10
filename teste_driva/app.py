import streamlit as st
import plotly.express as px
from etl import MarketData

etl = MarketData('data/Cópia de Teste visualização de dados.xlsx')
etl.load_sales()
etl.load_products()
etl.best_selling_days()
etl.daily_sales()
etl.sales_per_product()
etl.best_selling_product_in_kg()
etl.best_banana_selling_day()

st.title('Teste Driva - Análise de vendas na Feira')

st.header('Evolução do faturamento ao longo do tempo')
daily_sales = etl.con.execute("SELECT * FROM daily_sales").fetchdf()
fig = px.line(daily_sales, x='DATA', y='TOTAL_VENDA', title='Faturamento diário')
st.plotly_chart(fig)

if __name__ == '__main__':
    pass