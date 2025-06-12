# Write a program for elective subject after validating the available choices

class Choice:
    def __init__(self, name, r, subject):
        self.name = name
        self.roll = roll
        self.subject = subject

    def display(self):
        print("-------Student Information(-------")
        print("Name of student: ", self.name)
        print("Roll no of student: ", self.roll)
        print("Subject alloted: ", self.subject)

    @staticmethod
    def validate_subjet(subjects, x):
        if x in subjects:
            print('Option available')
            return True
        else:
            print('Option not available')
            return False
        
subjects = ["TAFL", "DS", "COA", "DLD"]
sub = input("Enter the subject of your choice: ")
if Choice.validate_subjet(subjects, sub):
    name = input("Enter your name: ")
    roll = int(input("Enter your roll: "))
    c = Choice(name, roll, sub)
    c.display()