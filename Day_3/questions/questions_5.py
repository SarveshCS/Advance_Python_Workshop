# Question 6 of Workshop pdf

class Employee:
    employee_count = 0
    organization_name = ""
    all_employees = []
    
    def __init__(self, name="", designation="", salary=0):

        self.name = name
        self.designation = designation
        self.salary = salary
        
        Employee.employee_count += 1
        Employee.all_employees.append(self)
    
    @classmethod
    def set_organization(cls, org_name):
        cls.organization_name = org_name
    
    def getdata(self):
        self.name = input("Enter employee name: ")
        self.designation = input("Enter employee designation: ")
        while True:
            try:
                self.salary = float(input("Enter employee salary: "))
                break
            except ValueError:
                print("Please enter a valid salary amount.")
    
    @classmethod
    def average(cls):
        if cls.employee_count == 0:
            return 0
        total_salary = sum(emp.salary for emp in cls.all_employees)
        return total_salary / cls.employee_count
    
    def display(self):
        print(f"Employee Information:")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: Rs. {self.salary:,.2f}")
        print("-" * 30)
    
    @classmethod
    def display_organization_info(cls):
        print(f"Organization: {cls.organization_name}")
        print(f"Total Employees: {cls.employee_count}")
        print(f"Average Salary: Rs. {cls.average():,.2f}")
        print("=" * 40)
    
    @classmethod
    def display_all_employees(cls):
        print(f"All Employees in {cls.organization_name}:")
        print("=" * 50)
        for i, emp in enumerate(cls.all_employees, 1):
            print(f"Employee {i}:")
            emp.display()
        cls.display_organization_info()


if __name__ == "__main__":
    Employee.set_organization("Tech Solutions Inc.")
    
    emp1 = Employee("Raju", "Software Engineer", 75000)
    emp2 = Employee("Rahul", "Project Manager", 85000)
    emp3 = Employee("Ram", "Data Analyst", 65000)
    
    print("Individual Employee Information:")
    emp1.display()
    emp2.display()
    emp3.display()
    
    Employee.display_organization_info()
    
    print("\nCreating a new employee interactively:")
    emp4 = Employee()
    emp4.getdata()
    
    emp4.display()
    # emp4.name = "Anurag"
    # emp4.designation = "Tech Lead"
    # emp4.salary = 5000000
    
    # print("\nUpdated organization information:")
    # Employee.display_all_employees()
