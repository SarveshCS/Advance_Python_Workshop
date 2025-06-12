class A:
    def __new__(cls):
        print("The new magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print("__int__ magic method is called")
        self.name = 'Python'


a = A()
print(a)