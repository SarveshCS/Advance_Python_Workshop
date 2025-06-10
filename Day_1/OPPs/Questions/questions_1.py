# Employee class - id, name, gender, designation | methods - display: 

class Employee:
    def __init__(self, id, name, gender, designation):
        self.id = id
        self.name = name
        self.gender = gender
        self.designation = designation

    def display(self):
        print(f"ID: {self.id}\nName: {self.name}\nGender: {self.gender}\nDesignation: {self.designation}")

emp1 = Employee(1, 'Sarvesh Mishra', 'Male', 'Teach Lead')
emp1.display()