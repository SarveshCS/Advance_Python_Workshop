class Animal:
    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

class Bird(Animal):
    def make_sound(self):
        print("Bird chirps")

# polymorphism in inheritance
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.make_sound()

print()

# Example 2
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 8)]

for shape in shapes:
    print(f"Area: {shape.area()}")