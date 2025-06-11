from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year): # this is a class method
        return cls(name, date.today().year - birth_year)
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")



rahul = Student('Rahul', 21)
rahul.display()

ram = Student.calculate_age("Ram", 2005)
ram.display()