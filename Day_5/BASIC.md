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

### Example 1 (abstract)

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

## Polymorphism

> Poly  -> Many
> Morph -> Ability to chnage

- Polymorphism in python is the abilty of an object to take many forms.
- It allows to perfom the same action in many different ways.

### Types of polymorphism

1. [Polymorphism in Operator](#1-polymorphism-in-operators)
2. [Polymorphism in Built-in Functions](#2-polymorphism-in-built-in-functions)
3. [Polymorphism in Class Methods](#3-polymorphism-in-class-methods)
4. [Polymorphism in Inheritance (Method overriding)](#4-polymorphism-in-inheritance-method-overriding)
5. [Method overloading](./polymorphism/method_overloading.py)
6. [Operator Overloading](./polymorphism/operator_overloading.py)

#### 1. Polymorphism in Operators

Example 1:

> **'+'**
>
> addition -> `5 + 2 = 7`
>
> concatination -> `'5' + '2' = '52`

Example 2:

> **'*'**
>
> multiplication -> `6 * 2 = 12`
>
> repetition -> `'8' * 3 = '888`

#### 2. Polymorphism in Built-in Functions

Example 1:

> **len()** Built-in
>
> It return length of iterables, and length of keys in dicts.
>
> Which means it works for different types of data, though it's the same function.

#### 3. Polymorphism in Class Methods

When we create different methods in different classes but with the same exact name.

Example 1:

```python
class Ferrari:
    def fuel_type(self):
        print('Petrol')
    def max_speed(self):
        print('Max speed is 350')

class BMW:
    def fuel_type(self):
        print('Diesel')
    def max_speed(self):
        print('Max speed is 240')

ferrari = Ferrari()
bmw = BMW()

for car in (ferrari, bmw):
    car.fuel_type()
    car.max_speed()
```

[Click here to check out this code](./polymorphism/class_method.py)

#### 4. Polymorphism in Inheritance (Method overriding)

Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

```python
class Animal:
    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# polymorphism in inheritance
animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()
```

[Click here to check out this code](./polymorphism/in_inheritance.py)

#### 5. Method Overloading

Two or more methods with the same name but different number of parameters.

Python doesn't support true method overloading like Java/C++, but we can simulate it using default parameters or `*args`.

[Click here to check out this code](./polymorphism/method_overloading.py)

#### 6. Operator Overloading

Operator overloading allows us to define custom behavior for operators when used with user-defined classes.

[Click here to check out this code](./polymorphism/operator_overloading.py)

### Dispatch Decorator

Will be used for method overloading

## Encapsulation

It is a mechanism of wrapping the data (variables) and code acting on the data (methods) togather as a single unit.

In encapsulation, the variables of a class will hidden from other classes. This hides the data and also make it easy for the other classes or the user to use it's functionality.

```python
class Computer:
    def __init__(self):
        self.__max_price = 1000
    
    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price
    
c = Computer()
c.sell()
c.set_max_price(2458)
c.sell()
print(c._Computer__max_price) # Way to access private class variable
```

[Click here to check out the code](./encapsulation/example_1.py)

## Acces Modifiers

1. Public
2. [Protected](#protected-modifier)
3. [Private]()

### Protected Modifier

Members of a class that are declared protected are only accessible to a class derived from it.

> Data members can be protected by adding a underscore (`_`) before the variable name.

Example 1:

```python
class Student:
    _name = None
    _roll = None
    _branch = None

    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
```

[Click here to check out this example](./access_modifier/example_1.py)