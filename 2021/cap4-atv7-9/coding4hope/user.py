from person import Person
from document import Document
from address import Address

class User(Person):
  """
  Entidade para reprentar um usuário do sistema
  """
  def __init__(self, first_name: str, last_name: str, document: Document, address: Address, email: str, password: str, is_admin: bool):
    super().__init__(first_name, last_name, document, address)
    self.email = email
    self.password = password
    self.is_admin = is_admin