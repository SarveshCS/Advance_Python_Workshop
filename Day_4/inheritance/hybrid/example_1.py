"""
Marks class inherits student class
Result inherits Sports class and Marks class
"""

class Student:
    def set_student_details(self, roll, name):
        self.roll = roll
        self.name = name

    def display_student_details(self):
        print(f"Name: {self.name}\nRoll no: {self.roll}\n")

class Marks(Student):
    def set_marks(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_marks(self):
        print(f"Marks 1: {self.marks1}\nMarks 2: {self.marks2}\nMarks 3: {self.marks1}\n")

class Sports:
    def set_sports_marks(self, m1):
        self.smarks = m1

    def display_sports_marks(self):
        print(f"P Marks: {self.smarks}\n")

class Result(Sports, Marks):
    def cal_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3 + self.smarks

    def display_result(self):
        print(f"Total marks: {self.total}\n")

re = Result()
re.set_student_details(1, 'Rahul')
re.display_student_details()
re.set_marks(85, 86, 89)
re.set_sports_marks(99)
re.display_marks()
re.display_sports_marks()
re.cal_total()
re.display_result()