CREATE TABLE IF NOT EXISTS dim_empresa (
    id_empresa INT PRIMARY KEY,
    nome_empresa VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_produto (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fato_vendas (
    id_venda INT PRIMARY KEY,
    id_empresa INT,
    id_produto INT,
    data_venda DATE,
    quantidade INT,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (id_empresa) REFERENCES dim_empresa(id_empresa),
    FOREIGN KEY (id_produto) REFERENCES dim_produto(id_produto)
);

