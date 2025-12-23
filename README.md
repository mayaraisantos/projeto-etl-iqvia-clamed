# Projeto ETL IQVIA – CLAMED

## 1. Introdução

Este projeto tem como objetivo desenvolver um processo de ETL (Extract, Transform, Load) para tratamento de dados de mercado fornecidos pela IQVIA, permitindo à CLAMED analisar sua posição frente aos concorrentes em diferentes regiões (Bricks).

Os dados originais são fornecidos em arquivos Excel (.xlsx) despadronizados, e o processo desenvolvido realiza a leitura, limpeza, transformação, integração com dados internos de filiais e armazenamento em um banco de dados PostgreSQL.

---

## 2. Tecnologias Utilizadas

- Python 3
- Pandas
- PostgreSQL
- SQLAlchemy / psycopg2
- Git e GitHub
- Google Colab
- Matplotlib

---

## 3. Estrutura do Projeto

```text
projeto-etl-iqvia-clamed/
│
├── data/
│   ├── MS_12_2022_sample.xlsx
│   └── filial-brick_sample.xlsx
│
├── notebooks/
│   └── analise_validacao.ipynb
│
├── sql/
│   └── create_tables.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
└── README.md
##4. Modelagem de Dados

O banco de dados foi modelado seguindo o modelo relacional, contendo as seguintes tabelas:

dim_filial_brick

Tabela de dimensão responsável por armazenar a relação entre filiais e seus respectivos bricks.

fact_vendas_iqvia

Tabela fato responsável por armazenar os volumes de vendas da IQVIA, incluindo:

Volumes de concorrentes

Volume da bandeira Preço Popular (PP)

Volume total de mercado

Participação da CLAMED

## 5.Extração

Leitura dos arquivos Excel fornecidos pela IQVIA e da planilha interna de filiais utilizando Pandas.

Transformação

Padronização dos nomes das colunas para snake_case

Conversão de tipos de dados (EAN para string)

Tratamento de valores nulos

Remoção de duplicatas

Criação das métricas:

vol_total_mercado

participacao_clamed

## 6.Carga

Conexão com o banco de dados PostgreSQL utilizando SQLAlchemy e inserção dos dados tratados nas tabelas do banco.

## 7.Validação e Análise

Para validação do processo de ETL, foi desenvolvido um notebook contendo:

Consulta dos dados integrados

Gráfico de barras comparando Volume PP e Volume Total de Mercado por Brick

Histograma da distribuição de vendas por produto (EAN)

Essas análises permitem validar a consistência dos dados carregados e gerar insights iniciais.
Como Executar o Projeto

Clonar o repositório

Instalar as dependências necessárias

Executar os scripts na seguinte ordem:

extract.py

transform.py

load.py

Executar o notebook analise_validacao.ipynb para validação dos dados

## Processo ETL

### Extract
Os dados são extraídos a partir de arquivos Excel fornecidos pela IQVIA.

### Transform
Nesta etapa são realizados:
- Padronização dos nomes das colunas
- Tratamento de valores nulos
- Remoção de registros duplicados
- Criação de colunas derivadas
- Junção entre tabelas

### Load
Os dados tratados são carregados em um banco PostgreSQL utilizando SQLAlchemy.

## Como executar o projeto
1. Instalar dependências: pip install pandas sqlalchemy psycopg2
2. Executar o pipeline: python src/main.py


