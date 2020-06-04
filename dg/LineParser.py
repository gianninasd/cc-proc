# class used to parse card request in CSV format
# throws validation errors if fields have errors
class LineParser:

  # parses a comma seperated string into each field
  # expected line format is
  # <merc ref>,<amount>,<card>,<expiry month>,<expiry year>,<first name>,<last name>,<email>,<postal code>
  def parse( self, line ):
    tokens = str(line).strip().split(',')

    data = {
      "merchantRefNum": tokens[0].strip(),
      "amount": int(tokens[1]),
      "settleWithAuth": "true",
      "card": {
        "cardNum": tokens[2],
        "cardExpiry": {
          "month": tokens[3],
          "year": tokens[4]
        }
      },
      "billingDetails": {
        "zip": tokens[8]
      }
    }

    return data