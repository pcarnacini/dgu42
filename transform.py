import pandas as pd
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Lê o csv que está na pasta csv/
df = pd.read_csv('csv/stgBancoVDE.csv')

# padroniza colunas convertendo texto em maíusculas
df = df.apply(lambda x: x.astype(str).str.upper())

# transforma os valores "NÃO INFORMADO" em "Desconhecido"
df = df.replace('NÃO INFORMADO', 'DESCONHECIDO')

# Faz a limpeza dos dados removendo todos os dados nulos e duplicados
df = df.dropna()
df = df.drop_duplicates()

# extrai ano e mês da coluna data, fazendo duas colunas separadas
df['DATA'] = pd.to_datetime(df['DATA'])  # Converte para datetime
df['ANO'] = df['DATA'].dt.year
df['MES'] = df['DATA'].dt.month
df['DIA'] = df['DATA'].dt.day_name

# remove a coluna data
df = df.drop(columns=['DATA'])

# remove a coluna formulário (não é relevante para a análise)
df = df.drop(columns=['FORMULARIO'])

# Função para obter latitude e longitude
def get_lat_long(uf, municipio):
        try:
            location = geolocator.geocode(f"{municipio}, {uf}, Brasil", timeout=10)
            if location:
                return pd.Series([location.latitude, location.longitude])
            else:
                return pd.Series([None, None])
        except GeocoderTimedOut:
            return pd.Series([None, None])
    
# Salvando o DataFrame em um novo arquivo CSV
df.to_csv('csv/dados_limpos.csv', index=False)