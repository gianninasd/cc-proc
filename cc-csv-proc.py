from dg.LineParser import LineParser
from dg.CardClient import CardClient
import os

# A Lambda function that processes the payload received from SQS.
def lambda_handler( event, context ):
  print('CC PY Reader received event..., invoked by {}'.format(context.invoked_function_arn ))
  #print('env: {}'.format(os.environ))

  parser = LineParser()
  client = CardClient(os.environ['CARD_URL'])

  # for each record, sends the txn print the response
  for item in event['Records']:
    data = parser.parse(item['body'])

    print("Sending: {}".format(data['merchantRefNum']))
    resp = client.send(data)
    print('Txn completed with code {} with data: {}'.format(resp.status_code, resp.json()))

