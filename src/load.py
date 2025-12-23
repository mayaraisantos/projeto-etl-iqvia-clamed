from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine(
        "postgresql+psycopg2://usuario:senha@localhost:5432/seu_banco"
    )

    df.to_sql(
        "fact_vendas_iqvia",
        engine,
        if_exists="replace",
        index=False
    )

    print("Carga concluída com sucesso no PostgreSQL")

