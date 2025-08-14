import os
import time
import pandas as pd
from GetBitCoin import get_bitcoin_df
from GetCommodities import get_commodities_df

SLEEP_SECONDS = 60
CSV_PATH = "cotacoes.csv"

# Criando o cabeçalho no CSV
if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):    # escreve o cabeçalho apenas uma vez
        cols = ['ativo', 'preco', 'moeda', 'horario_coleta']
        pd.DataFrame(columns=cols).to_csv(CSV_PATH, index=False)

# Fazendo Coleta e Inserindo os dados no CSV
while True:
    # Fazendo a coleta
    df_btc = get_bitcoin_df()
    df_cmd = get_commodities_df()

    # Juntanndo as duas extrações
    df = pd.concat([df_btc, df_cmd], ignore_index=True)

    # Salvando (append sem cabeçalho)
    df.to_csv(CSV_PATH, mode="a", header=False, index=False) #mode = "a" é para sempre ACRESCENTAR

    # Esperando próximo Ciclo
    time.sleep(SLEEP_SECONDS)
    
    print("Dados Inseridos com Sucesso!")

