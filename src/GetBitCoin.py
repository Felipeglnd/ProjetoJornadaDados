import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    # URL para obter o preço do BITCOIN
    URL = "https://api.coinbase.com/v2/prices/spot"

    # Requisição GET para API
    response = requests.get(URL)
    data = response.json()

    # Extração dos dados que serão utilizados
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_de_coleta = datetime.now()

    # Incluindo os dados no DateFrame
    df = pd.DataFrame([{
        'preco':preco,
        'ativo':ativo,
        'moeda':moeda,
        'horario_de_coleta':horario_de_coleta
    }])
    return df