import pandas as pd

# Lê o CSV da pasta csv/
df = pd.read_csv('csv/dados_limpos.csv')

# Converte a coluna 'feminino' para numérico, forçando valores inválidos para NaN
df['feminino'] = pd.to_numeric(df['feminino'], errors='coerce')

# Filtra apenas por estupro, feminicídio e homicídio doloso
df = df[df['evento'].isin(['Estupro', 'Feminicídio', 'Homicídio doloso'])]

# Remove todas as linhas onde 'feminino' é nulo, zero ou vazio
df = df[~((df['feminino'].isna()) | (df['feminino'] == 0) | (df['feminino'] == ''))]

# Salvando o DataFrame em um novo arquivo CSV
df.to_csv('csv/dados_estupro_feminicidio.csv', index=False)