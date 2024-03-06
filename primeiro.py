import pandas as pd
tabelas = pd.read_html("https://infomoney.com.br/cotacoes/empresas-b3/")

lista_empresas = []
for tabela in tabelas:
    lista_empresas.append(tabela.Ativos)

lista_empresas = [tabela.Ativos for tabela in tabelas]
empresas = []
for item in lista_empresas:
    empresas += list(item)

len(empresas)
    
