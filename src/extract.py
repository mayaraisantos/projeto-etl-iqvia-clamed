import pandas as pd

def extract_data():
    vendas = pd.read_excel("data/MS_12_2022_sample.xlsx")
    filial = pd.read_excel("data/filial-brick_sample.xlsx")
    return vendas, filial

