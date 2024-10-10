import pandas as pd 
import numpy as np
import duckdb

class MarketData:
    def __init__(self, data_path):   
        self.data_path = data_path
        self.con = duckdb.connect(database=':memory:')

    def load_sales(self):
        df = pd.read_excel(self.data_path, sheet_name='vendas', header=0, dtype=object)
        df['DATA'] = pd.to_datetime(df['DATA'], format='%d-%m-%y')
        df['VALOR_VENDA'] = pd.to_numeric(df['VALOR_VENDA']).round(2)
        # print(df.info())
        # print(df.head())
        # print(df.tail())
        self.con.execute("CREATE TABLE sales AS SELECT * FROM df")
        # result = self.con.execute("SELECT * FROM sales LIMIT 10").fetchall()
        # print(result)

    def load_products(self):
        df = pd.read_excel(self.data_path, sheet_name='produtos', header=0, dtype=object)
        self.con.execute("CREATE TABLE products AS SELECT * FROM df")
        # result = self.con.execute("SELECT * FROM products LIMIT 10").fetchall()
        # print(result)

    def best_selling_days(self): 
        result = self.con.execute("SELECT DATA, SUM(VALOR_VENDA) AS TOTAL_VENDA FROM sales GROUP BY DATA ORDER BY TOTAL_VENDA DESC LIMIT 10").fetchall()
        print(result)

    def daily_sales(self):
        result = self.con.execute("SELECT DATA, SUM(VALOR_VENDA) AS TOTAL_VENDA FROM sales GROUP BY DATA").fetchall()
        print(result)

    # def sales_per_product(self):
        # result = self.con.execute("SELECT ID_PRODUTO, SUM(VALOR_VENDA) AS TOTAL_VENDA FROM sales GROUP BY PRODUTO ORDER BY TOTAL_VENDA DESC").fetchall()
        # print(result)


    def count_abacaxi_sales(self):
        result = self.con.execute("SELECT 'A', p.NOME_PRODUTO, COUNT(p.ID_PRODUTO), SUM(s.VALOR_VENDA) AS TOTAL_VENDAS, SUM((s.VALOR_VENDA / p.PREÇO_KG)) AS Quantidade_Vendida_KG  FROM sales s INNER JOIN products p ON s.ID_PRODUTO = p.ID_PRODUTO WHERE p.NOME_PRODUTO = 'Abacaxi' GROUP BY p.NOME_PRODUTO").fetchall()
        print(result)

    def count_laranja_sales(self):
        result = self.con.execute("SELECT 'B', p.NOME_PRODUTO, COUNT(p.ID_PRODUTO), SUM(s.VALOR_VENDA) AS TOTAL_VENDAS, SUM((s.VALOR_VENDA / p.PREÇO_KG) * p.PESO_MEDIO_UNITARIO_KG) AS Quantidade_Vendida_KG FROM sales s INNER JOIN products p ON s.ID_PRODUTO = p.ID_PRODUTO WHERE p.NOME_PRODUTO = 'Laranja' GROUP BY p.NOME_PRODUTO").fetchall()
        print(result)

    def best_selling_product_in_kg(self):
        result = self.con.execute("SELECT 'C', p.NOME_PRODUTO, COUNT(p.ID_PRODUTO), SUM(s.VALOR_VENDA) AS TOTAL_VENDAS, SUM((s.VALOR_VENDA / p.PREÇO_KG)) AS Quantidade_Vendida_KG FROM sales s INNER JOIN products p ON s.ID_PRODUTO = p.ID_PRODUTO GROUP BY p.NOME_PRODUTO ORDER BY Quantidade_Vendida_KG DESC LIMIT 1").fetchall()
        print(result)

    def best_selling_product_in_kg_another_way_of_doing_it(self):
        result = self.con.execute("SELECT 'D', p.NOME_PRODUTO, COUNT(p.ID_PRODUTO), SUM(s.VALOR_VENDA) AS TOTAL_VENDAS, SUM((s.VALOR_VENDA / p.PREÇO_KG) * p.PESO_MEDIO_UNITARIO_KG) AS Quantidade_Vendida_KG FROM sales s INNER JOIN products p ON s.ID_PRODUTO = p.ID_PRODUTO GROUP BY p.NOME_PRODUTO ORDER BY Quantidade_Vendida_KG DESC LIMIT 1").fetchall()
        print(result)

    # def best_banana_selling_day(self):
    #     result = self.con.execute("SELECT EXTRACT(DAY FROM DATA) AS DAY, s.DATA, SUM(VALOR_VENDA) AS TOTAL_VENDA, COUNT(p.ID_PRODUTO) FROM sales s INNER JOIN products p ON s.ID_PRODUTO = p.ID_PRODUTO  WHERE p.NOME_PRODUTO = 'Banana' GROUP BY DAY, DATA ORDER BY TOTAL_VENDA DESC LIMIT 1").fetchall()
    #     print(result)
    

if __name__ == '__main__':
    data_path = 'data/Cópia de Teste visualização de dados.xlsx'
    market_data = MarketData(data_path) 
    market_data.load_sales()
    market_data.load_products()
    market_data.count_abacaxi_sales()
    market_data.count_laranja_sales()   
    market_data.best_selling_product_in_kg()
    market_data.best_selling_product_in_kg_another_way_of_doing_it()
    # market_data.best_selling_days()
    # market_data.daily_sales()
    # market_data.sales_per_product()
    # market_data.best_banana_selling_day()