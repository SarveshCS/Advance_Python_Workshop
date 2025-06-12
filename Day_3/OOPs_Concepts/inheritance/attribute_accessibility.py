class A:
    def setdataA(self):
        self.attr1 = 90
        self.__attr2 = 100

    def check(self):
        print("Inside Mehtod 1")
        print("Attribute 1:", self.attr1)
        print("Attribute 2:", self.__attr2)

class B(A):
    def setdataB(self):
        self.attr3 = 50
        self.__attr4 = 70
    
    def check2(self):
        print("Inside Mehtod 2")
        print("Attribute 3:", self.attr3)
        print("Attribute 4:", self.__attr4)
        print("Attribute 1:", self.attr1)

obj1 = B()
obj1.setdataA()
obj1.setdataB()

obj1.check()
obj1.check2()
