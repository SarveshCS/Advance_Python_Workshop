class A:
    def method(self):
        print("A.method() called")

class B:
    def method(self):
        print("B.method() called")

class C(A, B):
    pass

class D(C, B):
    pass

d = D()
d.method() # A.method() called
print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]