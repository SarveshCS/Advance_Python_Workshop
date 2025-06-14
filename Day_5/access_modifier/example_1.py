class Student:
    _name = None
    _roll = None
    _branch = None

    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _display_info(self):
        print("Roll: ", self._roll)
        print("Name: ", self._name)
        print("Branch: ", self._branch)

class NIET(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
    
    def display(self):
        print("Name: ", self._name)
        self._display_info()

N = NIET('XYZ', 103, 'CSE')
N.display()