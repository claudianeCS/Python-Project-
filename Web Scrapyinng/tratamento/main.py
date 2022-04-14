import pandas as pd

entrada = "promocao_mercado_livre.csv"
saida = 'resultado_promocao_mercado_livre.csv'

df = pd.DataFrame()

df = pd.read_csv(entrada, sep=',', header=0, usecols=['nome_do_produto', 'preco_original', 'desconto', 'preco_disconto'])

print(df)
df.replace('"', '')
df['desconto'] = df['desconto'].str.replace('%', '')

df.to_csv(saida, sep=';', encoding='utf-8')

print(df)

