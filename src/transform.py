import pandas as pd

def transform_data(vendas, filial):
    # padronização de colunas
    vendas.columns = vendas.columns.str.strip().str.lower().str.replace(" ", "_")
    filial.columns = filial.columns.str.strip().str.lower().str.replace(" ", "_")

    # tipos
    vendas['ean'] = vendas['ean'].astype(str)

    # tratamento de nulos
    vendas = vendas.fillna(0)

    # remoção de duplicatas
    vendas = vendas.drop_duplicates()

    # colunas derivadas
    vendas['mes_ano'] = pd.to_datetime(vendas['mes_ano'], format='%Y-%m')
    vendas['participacao_percentual'] = vendas['participacao_clamed'] * 100

    # merge
    df_final = pd.merge(vendas, filial, on="brick_id", how="left")

    return df_final

