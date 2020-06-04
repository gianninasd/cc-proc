#
class LineParser:

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