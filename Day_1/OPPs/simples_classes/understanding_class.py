class Student:
    class_var = 0     
    def __init__(self, var):       # Parameterized
        Student.class_var+=1
        self.var = var
        print("The object value is:", var)
        print("The value of class variable is:", Student.class_var)


Ram = Student(10)
Raju = Student(20)

print(Student.class_var)