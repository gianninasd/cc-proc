from dg.LineParser import LineParser
from dg.CardClient import CardClient

import unittest

# integration tests for the CardClient
class TestCardClient(unittest.TestCase):

  str = "jim7025,1500,4111111111111111,10,2020,Rick,Hunter,rick@sdf3.com,M5H 2N2"
  parser = LineParser()
  client = CardClient('https://e2u4zw2gvb.execute-api.us-east-2.amazonaws.com/Prod/cardSim')

  def test_SuccessfulTxn( self ):
    data = self.parser.parse(self.str)
    resp = self.client.send(data)
    obj = resp.json()

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(obj['merchantRefNum'], 'jim7025')
    self.assertEqual(obj['status'], 'COMPLETED')


if __name__ == '__main__':
  unittest.main()
