import streamlit as st
import plotly.express as px
from etl import MarketData
import os

data_path = os.path.abspath('data/Cópia de Teste visualização de dados.xlsx')
etl = MarketData(data_path=data_path)
etl.load_sales()
etl.load_products()
etl.best_selling_day()
etl.daily_sales()
etl.monthly_sales()
etl.sales_per_product()
etl.best_selling_product_in_kg()
etl.best_banana_selling_day()
etl.sales_by_time_range()



st.title('Teste Driva - Análise de vendas na Feira')

st.header('1 - Evolução do faturamento ao longo do tempo')
daily_sales = etl.con.execute("SELECT * FROM daily_sales").fetchdf()
monthly_sales = etl.con.execute("SELECT * FROM monthly_sales").fetchdf()
fig = px.line(daily_sales, x='DATA', y='TOTAL_VENDA', title='Faturamento diário')
fig2 = px.line(monthly_sales, x='MES', y='TOTAL_VENDA', title='Faturamento mensal')
st.plotly_chart(fig)
st.plotly_chart(fig2)

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

st.write('Alguns exemplos gráficos para se considerar ao buscar aumentar o faturamento: ')
data = etl.con.execute("SELECT * FROM sales_by_time_range").fetchdf()
# fig = px.density_heatmap(data, x='HORA', y='TOTAL', title='Heatmap de vendas por hora')
fig = px.bar(data, x='HORA', y='TOTAL', title='Vendas por hora')
st.plotly_chart(fig)

st.write('Relação entre peso do produto por KG e faturamento')
chart_data = etl.con.execute("SELECT * FROM sales_per_product").fetchdf()
st.scatter_chart(chart_data, x='PREÇO_KG', y='TOTAL_VENDA', x_label='PREÇO POR KG', y_label='TOTAL', color='NOME_PRODUTO')

if __name__ == '__main__':
    pass