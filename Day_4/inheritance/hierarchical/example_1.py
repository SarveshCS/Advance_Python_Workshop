class Parent:
    def meth1(self):
        print("This method is in the parent class")

class Child1(Parent):
    def meth2(self):
        print("This method is in the child 1")

class Child2(Parent):
    def meth3(self):
        print("This method is in the child 2")

obj1 = Child1()
obj1.meth1()
obj1.meth2()
# obj1.meth3()

obj2 = Child2()
obj2.meth1()
# obj2.meth2()
obj2.meth3()

obj_parent = Parent()
obj2.meth1()
# obj2.meth2() # Cant access
# obj2.meth3() # Cant access