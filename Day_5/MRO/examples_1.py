class A:
    def method(self):
        print("A.method() called")

class B(A):
    def method(self):
        print("B.method() called")

b = B()
b.method() # B.method() called
print(B.mro())  #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]