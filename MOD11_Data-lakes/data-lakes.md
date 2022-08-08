# Data lakes

- O que é um Data Lake?
- Camadas de um Data Lake
- Performance e particionamento dos dados
- Apache Parquet
- Criando um Data Lake com S3
- Boas práticas ao criar um Data Lake
<br />

---

## O que é um Data Lake?

"Um data lake é um repositório centralizado que permite que voce armazene todos os seus dados estruturados e não-estruturados em qualquer escala. Você pode armazenar os seus dados sem ter que primeiro estruturá-los, e então executar diferentes tipos de análises: de dashboards e visualizações, a processamento de big data, análise em tempo real e aprendizado de máquina.
<br />


Possíveis serviços a utilizar nas diferentes frentes de trabalho junto ao armazenamento:
<br /><br />

### 1. Central Storage

- S3 (simple storage service)

### 2. Data Ingestion (popular dados, inserir os dados no data lake)

- Lambda: para extrair dados de uma API e armazenar no repositório/ data lake
- DMS (Database Migration Service): para migrar dados de um banco de dados relacional para o data lake
- Kafka

### 3. Processing & Analytics

- Amazon Athena: permite fazer queries diretamente no S3
- Rodar Spark (engine de processamento de dados, de big data), via Amazon EMR, EC2, Databricks
- Redshift (p/ datawarehouse)
- Amazon QuickSight (dashboard)

### 4. Security & Governance

- AWS KMS
- AWS IAM
- AWS CloudTrail
- Amazon CloudWatch

### 5. Catalog & Search

Definição de catálogo de dados (metadados), em que se tem os schemas definidos, para poder exibir as tabelas.

- AWS Glue Catalog


### 6. User Access

Gerenciamento de acessos.

- AWS AppSync
- Amazon API Gateway
- Amazon Cognito

<br /><br />

---

## Camadas de um Data Lake
<br />

### **Camada 1 - raw, bronze**

Esta camada consiste em 1 ou mais buckets que armazenam os dados vindos dos serviços de ingestão. É importante que os dados armazenados nessa camada sejam mantidos e preservados em sua forma original e que nenhuma transformação de dados ocorra.

*Quem usa: Data Engineers, Jobs Spark*
<br /><br />

### **Camada 2 - processed, staged, silver**

Esta camada armazena os datasets resultantes da transformação dos dados brutos da camada 1 em arquivos colunares (como Parquet, ORC ou Avro) utilizando processamento ETL (por exemplo Spark, ou AWS Glue). Com os dados organizados em partições e em um formato colunar, os jobs de processamento conseguem ingerir estes dados com maior performance e menores custos.

*Quem usa: Data Scientists, Jobs Spark, DBT, Athena*
<br /><br />

### **Camada 3 - curated, enriched, gold**

Os dados armazenados nesta camada são um subgrupo da camada 2 que foram organizados para usos específicos. Os dados desta camada geralmente são acessados mais frequentemente por diversos stakeholders. Dependendo do uso de caso os dados podem ser servidos com diferentes tecnologias: Amazon EMR, Redshift, Presto, Athena, etc.

Nesta camada provavelmente serão trabalhados maiores processamentos:
- regras de negócio
- joins entre tabelas
- ...

*Quem usa: Data Analysts, Data Scientists, DW, Ferramentas de BI...*

<br /><br />

---

## Performance e particionamento dos dados

<br />

---

## Apache Parquet

É um formato opensource, mantido pela Apache. Trata-se de um arquivo de formato binário.

Comparação entre parquet e csv:
<br>

|       | Tamanho no S3 | Duração da query      | Dados escaneados | Custo da query  |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Dados armazenados como arquivos CSV | 1 TB | 236 segundos      | 1.15 TB | $5.75  |
| Dados armazenados no formato Apache Parquet | 130 GB | 6.78 segundos      | 2.51 GB | $0.01  |
| Economia      | Tamanho 87% menor ao usar parquet | 34x mais rápido      | 99% menos dados escaneados | 99.7% de economia  |


https://databricks.com/glossary/what-is-parquet

<br />

Um arquivo parquet é do tipo colunar, então desta forma ocorre a otimização de espaço, queries, etc.

<br />

---

## Criando um Data Lake com S3

- Create bucket
- Bucket name: **nomes de buckets são únicos em toda a AWS**
- AWS Region: especificar
- Block all public access
- Bucket versioning: Enable
- Tags: interessante para rastreamento dos custos
- Server-side encryption: Enable
- Encryption key type: especificar


<br />

---

## Boas práticas ao criar um Data Lake



