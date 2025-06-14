# Day 5

## Method Resolution Order (MRO)

MRo is a concept used in inheritance. It is the order in which a method is searched in class hiierchy and is especially useful in ython because it supports multiple types of inheritance.

- MRO is from bottom to top and left to right

### Example 1

```python
class A:
    def method(self):
        print("A.method() called")

class B(A):
    def method(self):
        print("B.method() called")

b = B()
b.method() # B.method() called
print(B.mro())  #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

[Click here to check out this code](./MRO/examples_1.py)

### Example 2

```python
class A:
    def method(self):
        print("A.method() called")

class B:
    def method(self):
        print("B.method() called")

class C(A, B):
    def method(self):
        print("C.method() called")

c = C()
c.method() # C.method() called
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

[Click here to check out this code](./MRO/examples_2.py)

### Example 3

```python
class A:
    def method(self):
        print("A.method() called")

class B:
    def method(self):
        print("B.method() called")

class C(A, B):
    pass

class D(C, B):
    pass

d = D()
d.method() # A.method() called
print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

[Click here to check out this code](./MRO/examples_3.py)

## Abstract class

- An `abstract` class is a class that can not be instanciated, however you can create classes that inherit from an `abstract` class.
- We use `abstract` class to create a bluerint for other classes.
- An `abstract` class may or may not include an `abstract` method

> ### Abstract method
>
> - It is a method without an implementation.

### Code to import abstract class, and method

```python
from abc import ABC, abstractmethod
```

### Example 1

```python
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
```

[Click here to check this out](./abstract_class/example_1.py)

> Q1. Create a abstract class name `Polygon`, create a abstract method named `number_of_sides`. Inherit this class in `Pentagon`, `Hexagon`, `Quadilateral`.

[Answer](./abstract_class/question_1.py)