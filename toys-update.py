import json

from dg.ToyValidator import ToyValidator


# Validates and updates the data for a toy entity
def update_toy(event, context):
  id = event['id']
  print('Updating toy {}'.format(id))

  val = ToyValidator()
  errors = val.validate(event)
  num_of_errors = len(errors)

  print('Updating toy {} - error count {}'.format(id, num_of_errors))

  if num_of_errors > 0:
    resp_json = {
      "statusCode": 400,
      "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      "body": errors
    }
    return resp_json
  else:
    return {
      "statusCode": 200,
      "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      "body": "{}"
    }
