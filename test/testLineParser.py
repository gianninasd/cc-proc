from dg.LineParser import LineParser

import unittest

# unit tests for the LineParser
class TestLineParser(unittest.TestCase):

  str = "jim7025,1500,4111111111111111,10,2020,Rick,Hunter,rick@sdf3.com,M5H 2N2"
  parser = LineParser()

  def test_GoodLine( self ):
    data = self.parser.parse(self.str)
    self.assertEqual(data['merchantRefNum'], 'jim7025')
    self.assertEqual(data['amount'], 1500)

if __name__ == '__main__':
  unittest.main()
