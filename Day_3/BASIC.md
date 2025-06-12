# Day 3

## 3. Static method

```python
class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

Employee.sample(10) ## Calling static method

Emp = Employee()
Emp.sample(10) # calling static method by virtue of an object
```

### Understanding the static method

[Click here to see a basic example](./staticmethod/basic.py)

## Difference between methods

> `class method` vs `instance method` vs `static method`

| Class method | vs | Instance method | vs | Static method |
|:------------:|:------------:|:-------------:|:------------:|:---------------:|
|Bound to the class||Bound to the object of the class||Bound to the class|
|It can modify a class state||It can modify an object state||It can't modify a class or object state|
|Can access only class variable||Can access and modify both class and instance variable||Can't access or modify the class or instance variable|

## Magic methods

These methods starts and end with a dunder (`__`), they are called by default on certain actions.

> when we add two integers using `+` operator it calles the `__add__` on one fo the `int` objects.

### new() magic method

It is called implicitly before the init method is called, it return a new objects which is then initialized by init

### str() magic method

It is overwritten to return a string representation of any user defined class.

> `__repr__` this method works similar to `__str__` though `__repr__` is generally used by the developers to get a verbose reponse about the class.
>
> `__repr__` stands for representation.

## Object Oriented Concept

It has four pillars

1. **Inheritance**: _Sharing Information_
2. **Abstraction**: _Hiding Information_
3. **Polymorphism**: _Redefining Informatiob_
4. **Data Encapsulation**: _Grouping Infromation_

### Inheritance

It refers to defining a new class, with little or no modification to a exiting class.
The new class is called a derived or child class and the one from which inherits is known as base class or parent class.

#### Benifits of Inheritance

- It provides the feature of reusability, which allows the user to add mroe features to the derived class without altering it.
- If a class `Y` inherits fromt he class `X` then, automatically all the subclasses of `Y` would inherit from class `X`.

#### Syntax

```psudo
class <class_name>[(parent_class)]:
    pass
```

#### Example

```python
class Person:
    pass

print(Person.__base__) # <class 'object'>

class Teacher(Person):
    pass

print(Teacher.__base__) # <class '__main__.Person'>
```

[Click here to check out this code](./OOPs_Concepts/inheritance/basic.py)

#### 1. Single Inheritance

```python
class A:
    def meth1(self):
        print('Inside Method 1')

    def meth2(self):
        print('Inside Method 2')

class B(A):
    def meth3(self):
        print('Inside Method 3')

obj1 = B()
obj1.meth1() # Inside Method 1
obj1.meth2() # Inside Method 2
obj1.meth3() # Inside Method 3

obj1 = A()
obj1.meth1() # Inside Method 1
obj1.meth2() # Inside Method 2
obj1.meth3() #AttributeError: 'A' object has no attribute 'meth3'. Did you mean: 'meth1'?
```

[Click here to check out this code](./OOPs_Concepts/inheritance/implementation.py)

#### Attributes Accessibility

```python
class A:
    def setdataA(self):
        self.attr1 = 90
        self.__attr2 = 100

    def check(self):
        print("Inside Mehtod 1")
        print("Attribute 1:", self.attr1)
        print("Attribute 2:", self.__attr2)

class B(A):
    def setdataB(self):
        self.attr3 = 50
        self.__attr4 = 70
    
    def check2(self):
        print("Inside Mehtod 2")
        print("Attribute 3:", self.attr3)
        print("Attribute 4:", self.__attr4)
        print("Attribute 1:", self.attr1)

obj1 = B()
obj1.setdataA()
obj1.setdataB()

obj1.check()
obj1.check2()
```

[Click here to check out this code](./OOPs_Concepts/inheritance/attribute_accessibility.py)
