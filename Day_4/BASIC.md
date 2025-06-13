# Day 4

> Continuation of Inheritance

## `super()`

It maked class inheritance code manageable and extensible.

It returns a temperory object, that allows reference to a parent class by the keyword `super`

It has two major usages:

- To avoid the usage of the parent class explicitly
- To enable multiple inheritance

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

obj1 = Square(5)
print(obj1.area())
```

[Click here to check out the above code](./inheritance/super_function.py)

> Types of Inheritance:
>
> - `Single Inheritance`
> - `Hierarchical Inheritance`
> - `Multilevel Inheritance`
> - `Multiple Inheritance`
> - `Hybrid Inheritance`

## Hierarchical Inheritance

More than one child class is being derived from a single parent class

```python
class Parent:
    def meth1(self):
        print("This method is in the parent class")

class Child1(Parent):
    def meth2(self):
        print("This method is in the child 1")

class Child2(Parent):
    def meth3(self):
        print("This method is in the child 2")

obj1 = Child1()
obj1.meth1()
obj1.meth2()
# obj1.meth3() # Can't acces

obj2 = Child2()
obj2.meth1()
obj2.meth2()
# obj2.meth3() # Cant access

obj_parent = Parent()
obj2.meth1()
# obj2.meth2() # Cant access
# obj2.meth3() # Cant access

```

[Click here to check out this example](./inheritance/hierarchical/example_1.py)

[Another example](./inheritance/hierarchical/example_2.py)

## Multilevel Inheritance

The technique of deriving a class from already derived class

Features of the base class and the derived classes are inherited into new derived class.

```python
class Student:
    def set_student_details(self, roll, name):
        self.roll = roll
        self.name = name

    def display_student_details(self):
        print(f"Name: {self.name}\nRoll no: {self.roll}\n")

class Marks(Student):
    def set_marks(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_marks(self):
        print(f"Marks 1: {self.marks1}\nMarks 2: {self.marks2}\nMarks 3: {self.marks1}\n")

class Result(Marks):
    def cal_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def display_result(self):
        print(f"Total marks: {self.total}\n")

re = Result()
re.set_student_details(1, 'Rahul')
re.set_marks(85, 86, 89)
re.display_student_details()
re.cal_total()
re.display_result()
```

[Click here to check out this example](./inheritance/multilevel/example_1.py)

## Multiple Inheritance

When a derived class inherts features from more than one base class it is called "Multiple Inheritance". The derived class has all the features of both the base classes and in addition to them, can have additional new features.

### Syntax

```python
class childClass(<Parent1>, <Parent2>):
    pass
```

### Example 1

```python
class Student:
    def set_student_details(self, roll, name):
        self.roll = roll
        self.name = name

    def display_student_details(self):
        print(f"Name: {self.name}\nRoll no: {self.roll}\n")

class Marks:
    def set_marks(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_marks(self):
        print(f"Marks 1: {self.marks1}\nMarks 2: {self.marks2}\nMarks 3: {self.marks1}\n")

class Result(Student, Marks):
    def cal_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def display_result(self):
        print(f"Total marks: {self.total}\n")

re = Result()
re.set_student_details(1, 'Rahul')
re.set_marks(85, 86, 89)
re.display_student_details()
re.cal_total()
re.display_result()
```

[Click here to check out this example](./inheritance/multiple/example_1.py)

## Hybrid Inheritance

It is a combination of muliple and multilevel inheritance.

```python
"""
Marks class inherits student class
Result inherits Sports class and Marks class
"""

class Student:
    def set_student_details(self, roll, name):
        self.roll = roll
        self.name = name

    def display_student_details(self):
        print(f"Name: {self.name}\nRoll no: {self.roll}\n")

class Marks(Student):
    def set_marks(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_marks(self):
        print(f"Marks 1: {self.marks1}\nMarks 2: {self.marks2}\nMarks 3: {self.marks1}\n")

class Sports:
    def set_sports_marks(self, m1):
        self.smarks = m1

    def display_sports_marks(self):
        print(f"P Marks: {self.smarks}\n")

class Result(Sports, Marks):
    def cal_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3 + self.smarks

    def display_result(self):
        print(f"Total marks: {self.total}\n")

re = Result()
re.set_student_details(1, 'Rahul')
re.display_student_details()
re.set_marks(85, 86, 89)
re.set_sports_marks(99)
re.display_marks()
re.display_sports_marks()
re.cal_total()
re.display_result()
```

[Click here to check out this example](./inheritance/hybrid/example_1.py)
