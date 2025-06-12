# Question 7 of Workshop pdf

class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.get_pi() * (self.radius**2)
    
    def circum(self):
        return 2 * self.get_pi() * self.radius
    
    @classmethod
    def get_pi(cls):
        return cls.PI
    
    def display(self):
        print(f"Area: {self.area():.2f}\nPerimeter: {self.circum():.2f}\n")

c1 = Circle(5)
c1.display()
