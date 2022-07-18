import boto3
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

# sqs = boto3.resource('sqs',
#          aws_access_key_id = getenv('ACCESS_ID'),
#          aws_secret_access_key = getenv('ACCESS_KEY'))

client = boto3.client(
  'sqs',
  aws_access_key_id = getenv('ACCESS_ID'),
  aws_secret_access_key = getenv('ACCESS_KEY'),
  region_name='us-east-1')

# client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/165172726588/api-pagamentos-consumidor-criado')
print(response)
