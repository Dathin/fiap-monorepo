from typing import List
from student import Student
from user import User


class Class:
    """
    Entidade para reprentar uma turma
    """
    def __init__(self, name: str, student: List[Student], responsible: User):
        self.name = name
        self.student = student
        self.responsible = responsible
