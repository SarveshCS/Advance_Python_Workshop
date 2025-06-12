class A:
    def meth1(self):
        print('Inside Method 1')

    def meth2(self):
        print('Inside Method 2')

class B(A):
    def meth3(self):
        print('Inside Method 3')

obj1 = B()
obj1.meth1()
obj1.meth2()
obj1.meth3()

obj1 = A()
obj1.meth1()
obj1.meth2()
obj1.meth3()