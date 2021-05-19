from address import Address


from address import Address
from document import Document

class  Person:
  """
  Entidade para reprentar uma pessoa
  """
  def __init__(self, first_name: str, last_name: str, document: Document, address: Address):
    self.first_name = first_name
    self.last_name = last_name
    self.document = document
    self.address = address

  def full_name(self):
    f'{self.first_name} {self.last_name}'
