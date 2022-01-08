import json

from dg.ToyValidator import ToyValidator


# Validates and updates the data for a toy entity
def update_toy(event, context):
  print('Updating toy {}'.format(event['id']))

  val = ToyValidator()
  errors = val.validate(event)

  if len(errors) > 0:
    return {
      "statusCode": 400,
      "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      "body": json.dumps(errors)
    }
  else:
    return {
      "statusCode": 200,
      "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      "body": "{'boo': 'test1'}"
    }
