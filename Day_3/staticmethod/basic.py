class A:
    x = 10
    def __init__(self, x):
        self.x = x
    
    def display(x):
        return x
    
a = A(5)

print(a.x)

print(A.x)

print(A.display(20))

print(a.display())