class Student:
    def set_student_details(self, roll, name):
        self.roll = roll
        self.name = name

    def display_student_details(self):
        print(f"Name: {self.name}\nRoll no: {self.roll}\n")

class Marks:
    def set_marks(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_marks(self):
        print(f"Marks 1: {self.marks1}\nMarks 2: {self.marks2}\nMarks 3: {self.marks1}\n")

class Result(Student, Marks):
    def cal_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def display_result(self):
        print(f"Total marks: {self.total}\n")

re = Result()
re.set_student_details(1, 'Rahul')
re.set_marks(85, 86, 89)
re.display_student_details()
re.cal_total()
re.display_result()