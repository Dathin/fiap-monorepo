from datetime import date
from student import Student
from user import User

class StudentNote:
  """
  Entidade para reprentar as notas dos usuários sobre os estudantes
  """
  def __init__(self, text: str, student: Student, author: User, created_at: date):
    self.text = text
    self.student = student
    self.author = author
    self.created_at = created_at