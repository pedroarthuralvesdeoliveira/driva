# Teste técnico para estágio em inteligência de mercado da Driva

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como resposta ao desafio de Inteligência de Mercado da Driva. O objetivo é analisar dados de vendas de uma feira e responder às seguintes questões:

1. Como está a evolução do faturamento em geral (todos os produtos)
2. Qual foi o melhor dia em vendas
3. Qual foi o dia em que mais se vendeu Bananas
4. Qual produto é vendido em maior quantidade (kg)
5. Sugestões de estratégias para aumentar o faturamento

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal
- **Poetry**: Gerenciamento de dependências
- **DuckDB**: Processamento de dados
- **Streamlit**: Visualização de dados
- **Pandas**: Manipulação de dados
- **Plotly**: Geração de gráficos

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.10
- Poetry

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/pedroarthuralvesdeoliveira/teste-driva.git
cd teste-driva
```

2. Instale as dependências com Poetry
```bash
poetry install
```

### Preparação dos Dados

1. Coloque seu arquivo XLSX de dados na pasta `teste-driva/data/`
2. O arquivo deve conter as seguintes colunas:
   - `id_produto` (será convertido para int)
   - `data` (formato esperado: yyyy/mm/dd)
   - `valor_venda` (será convertido para float com 2 casas decimais)
   - `faixa_horario` (formato esperado: HH:MM)

### Executando a Aplicação

```bash
poetry run streamlit run teste-driva/app.py
```

## 📁 Estrutura do Projeto

```
teste-driva/
├── README.md
├── pyproject.toml
├── teste-driva/
│   ├──  data/
│   │       arquivo.XLSX
│   └
    ├── __init__.py
│   ├── app.py           # Aplicação Streamlit
│   ├── etl.py           # Lógica de ETL
│   ├── data/            # Dados de entrada
└
```

## 🔍 Funcionalidades

### Análises Disponíveis
- Evolução diária do faturamento
- Identificação do melhor dia de vendas
- Análise de vendas por produto
- Sugestões estratégicas baseadas nos dados


## 📈 Exemplos de Visualizações

A aplicação Streamlit fornece:
1. Gráfico de linha mostrando a evolução do faturamento
2. Métricas destacando o melhor dia de venda
3. Análise de dia que mais teve vendas do produto Banana
4. Análise de produto mais vendido em quantidade (KG) 
5. Sugestões estratégicas baseadas nos dados

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Notas Adicionais

- Este projeto foi desenvolvido como parte de um desafio técnico
- Os dados utilizados são fictícios
- Todas as vendas são consideradas dentro de uma mesma região

## 📫 Contato

Pedro - [dev@pedrooliveira.tech]

Link do projeto: [https://github.com/pedroarthuralvesdeoliveira/teste-driva](https://github.com/pedroarthuralvesdeoliveira/teste-driva)