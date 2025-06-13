# Questions 17 of workshop pdf

class Employee:
    def __init__(self, id, name, designation):
        self.id = id
        self.name = name
        self.designation = designation
        self.manager = None
        self.team_lead = None
        
    def display_info(self):
        print(f"Employee id: {self.id}\nName: {self.name}\nDesignation: {self.designation}")
        if self.manager:
            print(f"Manager: {self.manager.name}")
        if self.team_lead:
            print(f"Team Leader: {self.team_lead.name}")
        print()

class TeamLeader(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, "Team Leader")
        self.employees = []

    def add_member(self, obj):
        obj.manager = self
        self.employees.append(obj)

    def display_info(self):
        super().display_info()
        print("Employess managed:")
        for employee in self.employees:
            print(f"\t{employee.name}")
        print()

class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, "Manager")
        self.employees = []

    def add_member(self, obj):
        obj.team_lead = self
        self.employees.append(obj)

    def display_info(self):
        super().display_info()
        print("Employess managed:")
        for employee in self.employees:
            print(f"\t{employee.name}")
        print()

rahul = Employee(1, 'Rhul', 'Web dev intern')
rahul.display_info()

ram = Manager(2, 'Ram')
ram.add_member(rahul)
ram.display_info()

ansh = TeamLeader(3, 'Ansh')
ansh.add_member(rahul)
ansh.display_info()

rahul.display_info()



