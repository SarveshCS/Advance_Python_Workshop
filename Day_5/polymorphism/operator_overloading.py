# Operator overloading in Python using magic methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)           # Point(3, 4)
print(p2)           # Point(1, 2)
print(p1 + p2)      # Point(4, 6)
print(p1 - p2)      # Point(2, 2)
print(p1 * 2)       # Point(6, 8)
print(p1 == p2)     # False

# Example 2: Book class
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 350)

print(book1)                    # Python Basics (200 pages)
print(book2)                    # Advanced Python (350 pages)
print(book1 + book2)            # 550
print(book2 > book1)            # True
