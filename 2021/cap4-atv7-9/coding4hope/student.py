from person import Person
from document import Document
from address import Address
from datetime import date

class Student(Person):
  """
  Entidade para reprentar um estudante
  """
  def __init__(self, first_name: str, last_name: str, document: Document, address: Address, sibling_name: str, date_of_birth: date):
    super().__init__(first_name, last_name, document, address)
    self.sibling_name = sibling_name
    self.date_of_birth = date_of_birth
