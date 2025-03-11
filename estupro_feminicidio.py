import pandas as pd
import os

# Lê o csv que está na pasta csv/
df = pd.read_csv('csv/dados_limpos.csv')

# Filtra apenas por estupro, feminicídio, homicídio doloso
df = df[df['evento'].isin(['Estupro', 'FEMINICÍDIO', 'HOMICÍDIO DOLOSO'])]

# Remove todos os registros em 'HOMICÍDIO DOLOSO' que 'feminino' é 0, nulo ou vazio
df = df[(df['evento'] == 'HOMICÍDIO DOLOSO') & (df['feminino'].isna() | (df['feminino'] == 0) | (df['feminino'] == ' '))]

# Salvando o DataFrame em um novo arquivo CSV
df.to_csv('csv/dados_estupro_feminicidio.csv', index=False)