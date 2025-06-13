class A:
    def learn(self):
        print("This is method 1 in class A")
class B:
    def learn(self):
        print("This is method 1 in class B")
class C:
    def learn(self):
        print("This is method 1 in class C")

class D(B, C):
    def learn(self):
        pass
a = A()
b = B()
c = C()
d = D()
