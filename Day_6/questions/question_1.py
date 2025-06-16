# Program to create iterator for fibbonaci series

class Fibb:
    def __init__(self, limit, a=0, b=1):
        self.a = 1
        self.b = b
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.limit < self.a:
            raise StopIteration
        
        tmp = self.a
        self.a = self.b
        self.b = self.a + self.b
        return tmp
    

limit = 5000
fibb = Fibb(limit)

for i in fibb:
    print(i)
    print()