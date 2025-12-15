-- Criação das tabelas do projeto

CREATE TABLE dim_filial_brick (
    brick TEXT PRIMARY KEY
);

CREATE TABLE fact_vendas_iqvia (
    brick TEXT,
    ean TEXT,
    cod_prod_catarinense INTEGER,
    vol_concorrente_si NUMERIC,
    vol_concorrente_so INTEGER,
    vol_pp NUMERIC,
    vol_total_mercado NUMERIC,
    participacao_clamed NUMERIC
);
