from extract import extract_data
from transform import transform_data
from load import load_data

vendas, filial = extract_data()
df_final = transform_data(vendas, filial)
load_data(df_final)
