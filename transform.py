import pandas as pd
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

# Lê o CSV na pasta csv/
df = pd.read_csv('csv/stgBancoVDE.csv', low_memory=False)

# Remove colunas desnecessárias (se existirem)
colunas_para_remover = ['agente', 'arma', 'faixa_etaria', 'nao_informado', 'total_peso', 'abrangencia', 'formulario','total']
df = df.drop(columns=[col for col in colunas_para_remover if col in df.columns], errors='ignore')

# Converte a data e extrai ano, mês e dia da semana
df['data_referencia'] = pd.to_datetime(df['data_referencia'], errors='coerce')
df['ano'] = df['data_referencia'].dt.year
df['mes'] = df['data_referencia'].dt.month
df['dia_semana'] = df['data_referencia'].dt.day_name()

# Converte os dias de inglês para português
dia_semana = {
    'Monday': 'Segunda',
    'Tuesday': 'Terça',
    'Wednesday': 'Quarta',
    'Thursday': 'Quinta',
    'Friday': 'Sexta',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# Converte os dias da semana na coluna 'dia_semana'
df['dia_semana'] = df['dia_semana'].map(dia_semana)

# Remove a coluna 'data_referencia' após extração das informações
df = df.drop(columns=['data_referencia'])

# Transforma todos os espaços vazios em 0
df = df.replace(' ', 0)

# Dicionário para mapear UFs para nomes completos
uf_para_nome = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

# Inicializa o geolocalizador com um tempo maior de timeout
geolocator = Nominatim(user_agent="pcarnacini_dgu42", timeout=15)

# Dicionário para armazenar coordenadas já buscadas (cache)
coord_cache = {}

# Função para obter latitude e longitude
def get_lat_long(municipio, uf):
    key = f"{municipio}, {uf}"
    
    if key in coord_cache:  # Verifica se já buscamos esse município antes
        return coord_cache[key]
    
    try:
        nome_estado = uf_para_nome.get(uf, uf)  # Obtém o nome completo do estado
        location = geolocator.geocode(f"{municipio}, {nome_estado}, Brasil")
        time.sleep(1)  # Delay para evitar bloqueio por muitas requisições
        if location:
            coord_cache[key] = (location.latitude, location.longitude)
            return coord_cache[key]
    except (GeocoderTimedOut, GeocoderServiceError, AttributeError) as e:
        print(f"Erro ao buscar coordenadas para {municipio}, {uf}: {e}")
    
    coord_cache[key] = (None, None)
    return (None, None)

# Aplica a função e cria colunas de latitude e longitude
df[['latitude', 'longitude']] = df.apply(lambda x: pd.Series(get_lat_long(x['municipio'], x['uf'])), axis=1)

# Salva o DataFrame limpo
df.to_csv('csv/dados_limpos.csv', index=False)