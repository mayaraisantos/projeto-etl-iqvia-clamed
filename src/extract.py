import pandas as pd

def extract_data():
    vendas = pd.read_excel("data/MS_12_2022_sample.xlsx")
    filial = pd.read_excel("data/filial-brick_sample.xlsx")

    print(f"Extração concluída: {vendas.shape[0]} registros de vendas")
    print(f"Extração concluída: {filial.shape[0]} registros de filiais")

    return vendas, filial

