import json
import requests


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

    # process response
    # if resp.status_code == 200:
    #   obj = resp.json()
    #   result = CardResponse(cardRequest.recordId, 'SUCCESS', cardRequest.ref)
    #   result.txnId = str(obj['id'])
    #   result.ref = str(obj['merchantRefNum'])
    #   result.status = str(obj['status'])
    # elif resp.status_code >= 400 or resp.status_code < 500:
    #   result = CardResponse(cardRequest.recordId, 'FAILED', cardRequest.ref)
    #   result.txnId = str(resp.json()['id'])
    #   result.ref = str(resp.json()['merchantRefNum'])
    #   errorObj = resp.json()['error']
    #   result.errorCode = errorObj['code']
    #   result.message = errorObj['message']
    # elif resp.status_code == 500:
    #   result = CardResponse(cardRequest.recordId, 'ERROR', cardRequest.ref)

    return resp