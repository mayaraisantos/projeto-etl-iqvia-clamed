import pandas as pd

def transform_data(vendas, filial):
    vendas.columns = vendas.columns.str.strip().str.lower().str.replace(" ", "_")
    filial.columns = filial.columns.str.strip().str.lower().str.replace(" ", "_")

    vendas['ean'] = vendas['ean'].astype(str)
    vendas = vendas.fillna(0)
    vendas = vendas.drop_duplicates()

    vendas['mes_ano'] = pd.to_datetime(vendas['mes_ano'], format='%Y-%m')
    vendas['participacao_percentual'] = vendas['participacao_clamed'] * 100

    df_final = pd.merge(vendas, filial, on="brick_id", how="left")

    print("Transformação concluída:")
    print("- Padronização de colunas")
    print("- Tratamento de nulos")
    print("- Remoção de duplicatas")
    print("- Criação de colunas derivadas")
    print(f"- Total final de registros: {df_final.shape[0]}")

    return df_final


