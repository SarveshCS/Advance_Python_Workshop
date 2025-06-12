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

```python

```