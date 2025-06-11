class NIET:
    branch_name = "Computer Science"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nBranch: {NIET.branch_name}")


def questions(cls):
    print("Below assignment is for Computer Science: ", cls.branch_name)

NIET.questions = classmethod(questions)

rahul = NIET('Rahul', 21)
rahul.display()

rahul.questions()