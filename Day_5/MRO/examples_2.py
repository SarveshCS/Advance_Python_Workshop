class A:
    def method(self):
        print("A.method() called")

class B:
    def method(self):
        print("B.method() called")

class C(A, B):
    def method(self):
        print("C.method() called")

c = C()
c.method() # C.method() called
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]