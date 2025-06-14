from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(Self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
rec = Rectangle(5, 6)
print(rec.area())
    

