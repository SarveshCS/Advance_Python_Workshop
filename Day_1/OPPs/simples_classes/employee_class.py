class Employee:
    holiday = 10

sarvesh = Employee()
anurag = Employee()

sarvesh.name = 'Sarvesh'
sarvesh.salary = 10000
sarvesh.role = 'CTO'

anurag.name = 'anurag'
anurag.salary = 9000
anurag.role = 'Teach Lead'

# print(sarvesh.name)
# print(sarvesh.salary)
# print(sarvesh.role)
# print(sarvesh.__dict__)
# print(sarvesh.holiday)
print(Employee.holiday)

Employee.holiday = 20
print(Employee.holiday)
# print(Employee.__dict__)
anurag.holiday = 30
print(anurag.holiday)
print(sarvesh.holiday)
# print(anurag.__dict__)
print(Employee.holiday)
# print(Employee.__dict__)
# print(anurag.name)
# print(anurag.salary)
# print(anurag.role)
# print(anurag.__dict__)
# print(anurag.holiday)
# print(Employee.holiday)