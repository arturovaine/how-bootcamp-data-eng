# Amazon S3 - Simple Storage Service

"S3 parece ter uma estrutura de pastas, porém, por baixo dos panos não são pastas. S3 é como se fosse uma pasta gigante e é possível adicionar os prefixos, como se fossem pastas." S3 é o hd, voce pode implantar hdfs sobre o s3 - (Hadoop) HDFS.

Valores de custos em jun/2021:

> Primeiros 50 TB/mês -> 0.023 USD por GB

Outra parte de custo é de solicitação:

> S3 Standard -> 0.005 USD / Solicitações PUT, COPY, POST

<br />

# Amazon RDS (Relational Database Service)

Serviço de banco de dados relacionais na nuvem. Faz todo o provisionamento de hardware, configuração de banco de dados, aplicação de patches e backups. Está disponível em vários tipos de instâncias de banco de dados e oferece seis mecanismos de bancos de dados comuns, incluindo Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database e SQL Server.

- RDS é otimizado para INSERT, DELETE e UPDATES (banco OLTP - Online Transaction Processing)

Aurora -> serverless

<br />

## Instâncias:

- Escalabilidade vertical: limitado ao tamanho máximo de instâncias

- Escalabilidade horizontal: limitado ao número de instâncias, ao budget $

<br />

# Amazon Redshift

> Redshift = OLAP (Online Analytical Processing), otimizado para SELECT

Serviço de armazenamento de dados em escala de petabytes totalmente gerenciado na nuvem. Você pode começar com apenas algumas centenas de gigabytes de dados e escalar para um petabyte ou mais. Isso permite que você use seus dados para adquirir novos insights para seus negócios e clientes.

Possível fluxo:

RDS -> S3 -> Athena/Presto/Spark ou Redshift (datawarehouse)

<br />

# Amazon DynamoDB

Banco de Dados NoSQL para valores-chave e documentos. O DynamoDB pode processar mais de 10 trilhões de solicitações por dia e comportar picos de mais de 20 trilhões de solicitações por segundo. Útil para aplicações que precisam de acesso a dados com baixa latência em qualquer escala.

> É possível salvar JSON no Dynamo (por ser NoSQL)

<br />

# Amazon Elastic Compute Cloud (EC2)

Serviço de servidores virtuais. Facilita a computação em nuvem na escala da web para os desenvolvedores.

"É a ferramenta mais comum, básica, de processamento. S3 seria como um hd e o EC2 o processador e a memória para os teus dados."

EC2 pode ser utilizado para rodar docker (ou ECS, próprio para containers), AirFlow...

# Database Migration Service (DMS)

"O AWS Database Migration Service serve para migrar bancos de dados. Com o DMS, o banco de dados de origem permanece totalmente operacional durante a migração. E o DMS pode migrar dados de/para a maioria dos bancos de dados comerciais e de código aberto mais usados."

<br />

# AWS Lambda

Serviço de computação sem servidor, que permite execução de código sem provisionar ou necessidade de gerenciar servidores. Com Lambda você pode executar o código para praticamente qualquer tipo de aplicação ou serviço de back-end, tudo sem precisar de administração. Basta realizar o upload do seu código como um arquivo ZIP ou imagem de container, e Lambda aloca recursos de maneira automática.

<br />

# Amazon EMR (Amazon Elastic MapReduce)

Plataforma de big data para processar grandes quantidades de dados usando ferramentas de código aberto, como Apache Spark, Apache Hive, Apache HBase, 
Apache Flink, Apache Hudi e Presto. O Amazon EMR facilita a configuração, operação e escala de seus grandes ambientes de dados.

<br />

# Databricks

Similar ao EMR, mas de usabilidade mais amigável.

<br />

# AWS Glue Jobs

"Serviço de integração de dados sem servidor, que facilita descobrir, preparar e combinar dados para análise, machine learning e desenvolvimento da aplicação. Ele oferece todos os recursos necessários para a integração dos dados, portanto é possível começar a analisar seus dados e usá-los em minutos, ao invés de meses."

<br />

# Amazon Kinesis

## Kinesis Data Streams

Servidor, é necessário provisionar recursos (shard)

<br />

## Kinesis Data Firehose

Delivery stream, para persistir os dados, enviar para o S3 por exemplo.

"Serviço para carregar de forma confiável dados de streaming em data lakes, datastores e serviços de análises. Ele pode capturar, transformar e entregar dados de streaming para os serviços Amazon S3, Amazon Redshift e Amazon Elasticsearch Service. Ele também pode separar em lotes, compactar, transformar e criptografar streams de dados antes de carregá-los, o que minimiza o volume de armazenamento usado e aumenta a segurança."

<br />

## Kinesis Data Analytics

Queries, recursos de análise. SQL ou Apache Flink

<br />

# Amazon Athena

"O Amazon Athena é um serviço de consultas interativas que facilita a análise de dados no Amazon S3 usando SQL padrão. O Athena não precisa de servidor. Portanto não há infraestrutura para gerenciar e você paga apenas pelas consultas executadas."

<br />

# Amazon SageMaker

"Serviço para ajudar cientistas e desenvolvedores de dados a preparar, criar, treinar e implantar modelos de machine learning de alta qualidade rapidamente, reunindo um amplo conjunto de recursos criados especificamente para ML."

<br />

# Amazon CloudWatch

"Serviço de monitoramento e observação criados para engenheiros de DevOps, desenvolvedores, SREs e gerentes de TI. O CloudWatch fornece dados e insights práticos para monitorar aplicativos, responder às alterações de performance e otimizar a utilização de recursos.

O CloudWatch coleta dados de monitoramento e operações na forma de logs, métricas e eventos, oferecendo uma visualização unificada dos recursos, dos aplicativos e dos serviços da AWS executados na AWS e em servidores locais."

<br />

# Amazon Cloudformation

Similar ao Terraform (que é mais amigável, mais recomendável).

Infraestrutura como código. Utilizado para modelar uma coleção de recursos da AWS e provisioná-los com rapidez e consistência. Um template do CloudFormation descreve os recursos desejados e suas dependências para que você possa iniciá-los e configurá-los em conjunto como uma stack. Você pode usar um template para criar, atualizar e excluir uma stack inteira como uma única unidade, quantas vezes quiser, em vez de gerenciar os recursos individualmente."

<br />

# Amazon CLI (command line interface)

Ferramenta unificada para o gerenciamento de seus serviços na AWS. Com apenas uma ferramenta para fazer download e configurar, você poderá controlar vários serviços da AWS pela linha de comando e automatizá-los usando scripts.

<br />

# Amazon Boto3

SDK (software development kit) para Python


----------------------------------------------------------------

<br />

# AWS CLI:

Copiar um arquivo da área de trabalho para o um bucket no S3:


```bash
aws s3 cp Desktop/arquivo.csv s3://data/.../arquivo.csv --profile aws_arturo
```






Outros serviços de fora:

- Pentaho
- Clickhouse
- Prefect.io





