import json
from datetime import datetime
from faker import Faker
import time
import boto3
# from botocore.exceptions import ClientError
# from botocore import exceptions
# import logging
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

s3 = boto3.resource('s3',
         aws_access_key_id = getenv('ACCESS_ID'),
         aws_secret_access_key = getenv('ACCESS_KEY'))

client = boto3.client(
  'sns',
  aws_access_key_id = getenv('ACCESS_ID'),
  aws_secret_access_key = getenv('ACCESS_KEY'),
  region_name='us-east-1')
  
faker_instance = Faker()

def get_data():
    lat, lng, region, country, timezone = faker_instance.location_on_land()
    created_datetime = datetime.utcnow()
    return dict(
        created_at=f"{datetime.utcnow()}",
        updated_at=f"{datetime.utcnow()}",
        customer_id=faker_instance.uuid4(),
        name=faker_instance.name(),
        region=region,
        country=country,
        lat=lat,
        lng=lng,
        email=faker_instance.ascii_free_email(),
        phone=faker_instance.phone_number()
    )

while True:
    data = get_data()
    client.publish(
        TopicArn='arn:aws:sns:us-east-1:165172726588:consumidor-criado',
        Message= json.dumps(data)
    )
    print(data)
    time.sleep(1)
