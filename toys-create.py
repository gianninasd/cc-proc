import boto3

from dg.ToyValidator import ToyValidator


# Validates and create the data for a toy entity
def update_toy(event, context):
  print('Creating toy for {}'.format(context.aws_request_id))