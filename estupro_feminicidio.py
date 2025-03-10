import pandas as pd
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Lê o csv que está na pasta csv/
df = pd.read_csv('csv/stgBancoVDE.csv')

# Obtém o percentual de vítimas femininas
df['percentual_feminino'] = (df['feminino']/df['total'])
df['soma_consistente'] = df['feminino'] + df['masculino'] + df['nao_informado']
df['total'] != df['soma_consistente']

# Codifica as variáveis categóricas
df['e_estupro'] = df['evento'].str.upper().apply(lambda x: 1 if x == 'ESTUPRO' else 0)
df['e_feminicidio'] = df['evento'].str.upper().apply(lambda x: 1 if x == 'FEMINICÍDIO' else 0)

# Salvando o DataFrame em um novo arquivo CSV
df.to_csv('csv/dados_estupro_feminicidio.csv', index=False)