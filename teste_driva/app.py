import streamlit as st
import plotly.express as px
from etl import MarketData

etl = MarketData('data/Cópia de Teste visualização de dados.xlsx')
etl.load_sales()
etl.load_products()
etl.best_selling_day()
etl.daily_sales()
etl.sales_per_product()
etl.best_selling_product_in_kg()
etl.best_banana_selling_day()

st.title('Teste Driva - Análise de vendas na Feira')

st.header('1 - Evolução do faturamento ao longo do tempo')
daily_sales = etl.con.execute("SELECT * FROM daily_sales").fetchdf()
fig = px.line(daily_sales, x='DATA', y='TOTAL_VENDA', title='Faturamento diário')
st.plotly_chart(fig)

st.header('2 - Melhor dia em vendas')
best_day, best_revenue = etl.best_selling_day()
st.write(f'O melhor dia em vendas foi {best_day} com um faturamento de R${best_revenue:.2f}')

st.header('3 - Dia que mais vendeu bananas')
date, revenue, count = etl.best_banana_selling_day()
st.write(f'O dia que mais vendeu bananas foi {date} com um faturamento de R${revenue:.2f} e {count} vendas')

st.header('4 - Produto que vende em maior quantidade (KG)')
product, count, revenue, kg = etl.best_selling_product_in_kg()
st.write(f'O produto que vende em maior quantidade é {product} com {count} vendas e um faturamento de R${revenue:.2f} e {kg:.2f} KG vendidos')

st.header('5 - Estratégias para aumentar o faturamento')
st.write("""
-  **Foco em dias de pico**: Investir em promoções e descontos em dias de pico de vendas.
-  **Otimização de mix de produtos**: Priorizar produtos com maior margem de lucro.
-  **Promoções direcionadas**: Criar promoções direcionadas para produtos com menor saída ou em dias de baixo movimento.
""")

if __name__ == '__main__':
    pass