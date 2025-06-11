class NIET:
    branch_name = "Computer Science"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_branch(cls, branch_name): # this is a class method
        NIET.branch_name = branch_name
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nBranch: {NIET.branch_name}")



rahul = NIET('Rahul', 21)
rahul.display()
NIET.change_branch = "AIML"
rahul.display()