import json
import requests

# Client class used to call an external REST API for transaction processing
class CardClient:
  cardUrl = ''

  # constructor
  def __init__( self, cardUrl ):
    self.cardUrl = cardUrl

  # sends a purchase request to a remote REST API
  def send( self, data ):
    url = self.cardUrl
    headers = {'content-type': 'application/json'}

    # send the request
    resp = requests.post(url, headers=headers, data=json.dumps(data))

    return resp