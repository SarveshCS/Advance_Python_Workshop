class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self):
        print(f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}')

raju = Person('Raju', 18, 'Male')

raju.display()