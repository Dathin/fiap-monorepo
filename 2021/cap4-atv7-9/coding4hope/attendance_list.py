from class import Class
from datetime import date
from student import Student
from typing import Dict


class AttendanceList:
    """
    Entidade para reprentar uma lista de presença
    """
    def __init__(self, fill_date: date, list: Dict[Student, bool], class: Class):
        self.fill_date = fill_date
        self.list = list
        self.class = class
