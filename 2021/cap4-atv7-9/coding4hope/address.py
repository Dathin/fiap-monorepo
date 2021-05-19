class Address:
  """
  Entidade para reprentar um endereço
  """
  def __init__(self, state: str, city: str, street: str, number: int, zipcode: str, complement: str):
    self.state = state
    self.city = city
    self.street = street
    self.number = number
    self.zipcode = zipcode
    self.complement = complement

  def format_address(self):
    """
    Devolve o endereço completo formatado
    """
    return f'{self.street} {self.number} {self.complement}, {self.zipcode}, {self.city} - {self.state}'