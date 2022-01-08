
# validates the fields of a toy object
class ToyValidator:

  # runs the main validate logic, various fields in the object will be evaluated
  def validate(self, obj):
    errors = {}

    if not self.valid_len(obj.get('name'), 1, 50):
      errors['name'] = 'Field must be provided'

    if not self.valid_len(obj.get('model'), 1, 50):
      errors['model'] = 'Field must be provided'

    try:
      pieces = int(obj.get('pieces'))

      if pieces is None:
        errors['pieces'] = 'Must be a valid number'
      elif pieces < 0:
        errors['pieces'] = 'Must be a valid number'
    except Exception as ex:
      # print('Unable to verify pieces field: {}'.format(ex))
      errors['pieces'] = 'Must be a valid number'

    try:
      purchaseYear = int(obj.get('purchaseYear'))

      if purchaseYear is None:
        errors['purchaseYear'] = 'Must be a valid number'
      elif purchaseYear < 2000 or purchaseYear > 2022:
        errors['purchaseYear'] = 'Must be a valid number'
    except Exception as ex:
      # print('Unable to verify pieces field: {}'.format(ex))
      errors['purchaseYear'] = 'Must be a valid number'

    return errors

  # validates the min and max length of a value
  def valid_len(self, value, min, max):
    if value is None:
      return False
    elif len(value) < min:
      return False
    elif len(value) > max:
      return False
    else:
      return True
