import pandas as pd 
import numpy as np
import duckdb

class MarketData:
    def __init__(self, data_path):   
        self.data_path = data_path
        self.con = duckdb.connect(database=':memory:')

    def load_sales(self):
        df = pd.read_excel(self.data_path, sheet_name='vendas', header=0, dtype=object)
        self.con.execute("CREATE TABLE sales AS SELECT * FROM df")
        # result = self.con.execute("SELECT * FROM sales LIMIT 10").fetchall()
        # print(result)

    def load_products(self):
        df = pd.read_excel(self.data_path, sheet_name='produtos', header=0, dtype=object)
        self.con.execute("CREATE TABLE products AS SELECT * FROM df")
        # result = self.con.execute("SELECT * FROM products LIMIT 10").fetchall()
        # print(result)

    def 

if __name__ == '__main__':
    data_path = 'data/Cópia de Teste visualização de dados.xlsx'
    market_data = MarketData(data_path) 
    market_data.load_sales()
    market_data.load_products()