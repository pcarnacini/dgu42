import pandas as pd
import os

# xlsx/ é onde estão todos os arquivos .xlsx e deve salvar na pasta csv o stgBancoVDE.csv
pd.concat([pd.read_excel(f'xlsx/{f}') for f in os.listdir('xlsx')]).to_csv('csv/stgBancoVDE.csv', index=False)