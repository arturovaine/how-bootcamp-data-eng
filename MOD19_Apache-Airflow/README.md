# MOD19_AIRFLOW

## Links

[Airflow](https://airflow.apache.org/)

[Documentação](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

[Dados COVID19](https://dados.gov.br/dataset/registro-de-ocupacao-hospitalar)

## Tipos de operadores para DAGS

- BashOperator: executa comandos shellscript
- DummyOperator: cria um nó que não executa nada, somente para representação
- EmailOperator: envia e-mail
- HdfsOperator: aguarda por um arquivo ou pasta no HDFS
- HiveOperator: executa código hql em um banco de dados Hive específico
- SimpleHttpOperator: faz uma requisição de um endpoint HTTP
- MySqlOperator: executa códigos SQL em um banco MySQL
- PostgresOperator: executa códigos SQL em um banco PostgreSQL
- PythonOperator: executa um código callable em Python
