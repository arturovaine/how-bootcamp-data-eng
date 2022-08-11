# AWS Glue e Athena

- Introdução ao AWS Glue
- O que são metadados
- Databases, Crawlers e Tables
- Introdução ao AWS Athena
- Queries no Data Lake utilizando o Athena
<br />

---

## Introdução ao AWS Glue

" AWS Glue is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced in August 2017."

AWS Glue is a fully managed ETL (extract, transform and load) service.

ETL -> verificar o Databricks


No Glue é interessante a parte de catálogo.

Catálogo é baseado no Apache Hive (hive.apache.org), ferramenta opensource. O AWS Glue foi construído sobre o Hive, é como se fosse um hive gerenciado, "pré-configurado". Além disto, o Glue tem como uma das facilidades os Crawlers. 

<br />

---

## O que são metadados

Metadados: dados sobre os dados.

Exemplo:



```
Tipo de arquivo: CSV

Localização: s3://data-lake-raw/arquivo.csv


Compressão: GZIP

Schema:
  customer_id, string
  created_at, date
  name, string
  ...

Tamanho: 2Mb

Nome da tabela: consumidores

Nome da database: app

```

Ferramentas que podem acessar os metadados:

- Athena
- Spark
- Presto


Etapas:

1. Leitura de metadados
2. Leitura dos dados


<br />

---

## Databases, Crawlers e Tables

### Database

> "A database is a set of associated table definitions, organized into a logical group."



<br />

---
## Introdução ao AWS Athena

<br />

---
## Queries no Data Lake utilizando o Athena


<br />

---

<br />