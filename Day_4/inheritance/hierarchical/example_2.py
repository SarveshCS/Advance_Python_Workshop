class Person:
    def setDetails(self, name, age):
        self.name = name
        self.age = age

    def displayDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Teacher(Person):
    def setTeacherDetails(self, subject, exp):
        self.subject = subject
        self.exp = exp

    def displayTeacherDetails(self):
        print(f"Subject: {self.subject}\nExperience: {self.exp} years\n")

class Student(Person):
    def setStudentDetails(self, roll, branch):
        self.roll = roll
        self.branch = branch

    def displayStudentDetails(self):
        print(f"Roll no: {self.roll}\nBranch: {self.branch}\n")

T1 = Teacher()
T1.setDetails('Rahul', 45)
T1.displayDetails()
T1.setTeacherDetails('DSA', 5)
T1.displayTeacherDetails()

S1 = Student()
S1.setDetails('Ram', 19)
S1.displayDetails()
S1.setStudentDetails(2366, 'CSE')
S1.displayStudentDetails()
