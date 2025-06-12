# Question 4 of Workshop pdf

class Number:
    MULTIPLIER = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER
    
    @staticmethod
    def subtract(b, c):
        return b - c
    
    def value(self):
        return self.x, self.y

num1 = Number(5, 6)
print(num1.add())
print(num1.value())

print(Number.multiply(3))
print(Number.subtract(5, 3))