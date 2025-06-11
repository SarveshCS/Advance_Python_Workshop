class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area: {self.length * self.width}")
        return None
    
rect1 = Rectangle(5, 10)
rect1.area()