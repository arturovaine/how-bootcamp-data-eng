# Introdução à AWS

- Criar uma conta e configurar o AWS CLI
- Criar alertas de budget
- Ativar a autenticação por duas camadas
- Criar usuários
- Overview de serviços para dados e Boto3


## O que é

Amazon Web Services é a plataforma de nuvem mais adotada e mais abrangente do mundo, oferencendo mais de 175 serviços completos de datacenters em todo o mundo.

https://www.visualcapitalist.com/aws-powering-the-internet-and-amazons-profits/

## Criar uma conta

- Cartão de crédito para cadastro (considerar cartão virtual)
- Utilizar senha segura
- Ativar autenticação multifator (MFA)
- Ativar alarme de faturamento/cobrança
- Deletar/desativar imediatamente todos os recursos que você criou para prototipar/testar, mesmo que esteja no free-tier

No cadastro, é possível utilizar um `alias` da seguinte forma, no login:

`seu-email-normal+alias@email.com`

em que `+alias` será "desconsiderado" e conta estará associada ao email sem `+alias`

## Criando usuários e Boto3

### Criando usuário no serviço `IAM`

Definir:

- Nome de usuário
- Tipo de acesso (default: Acesso programático)
- Permissões (Anexar políticas, ex.: S3, ...)
- -> Revisar e Criar usuário

Com usuário criado, são mostrados os dados:
- Usuário (nome)
- ID da chave de acesso (ex.: AKIAAIUTT...)
- Chave de acesso secreta

Em seguida, em um ambiente virtual iniciar a implementação:

```bash
pip install pandas ipython boto3 python-dotenv
```

Boto3 é o pacote que permite acesso à API da Amazon.

Em arquivo `.env` criar variáveis de ambiente:

```.env
AWS_ID = ...
AWS_KEY = ...
```

Em novo arquivo `aws.py`:

```Python
#%%
import boto3 # integração com API AWS
from botocore import exceptions # tratamento de erros
from botocore.exceptions import ClientError # tratamento de erros
import logging # logs
from dotenv import load_dotenv # p/ carregar variáveis de ambiente
from os import getenv # acessar variáveis de ambiente

#%%
load_dotenv(/.env)

#%%
getenv('AWS_ID')

#%%
# Criar um client

s3_client = boto3.client(
  's3',
  aws_access_key_id = getenv('AWS_ID'),
  aws_secret_access_key = getenv('AWS_KEY')
)

#%%
# Função para criar bucket s3

def criar_bucket(nome):
  try:
    s3_client.create_bucket(Bucket=nome)
  except ClientError as e:
    logging.error(e)
    return False
  return True

#%%
# Timestamp

from datetime import datetime

def timestamp():
  d = datetime.today()
  timestamp = d.strftime('%Y-%m-%d_%Hh%Mm%Ss')
  return timestamp

# Retorna data no formato: '2022-08-05_09h30m30s'

#%%
# Então é possível utilizar a função acima para o nome do bucket

criar_bucket('s3-bucket-'+timestamp())
# Se retornar True, criação foi realizada com sucesso

```