from extract import extract_data
from transform import transform_data
from load import load_data

print("Iniciando pipeline ETL...")

vendas, filial = extract_data()
df_final = transform_data(vendas, filial)
load_data(df_final)

print("Pipeline ETL finalizado com sucesso")
