# Constructor in python

1. A constructor can simply be defined as a special method, which can be used to initialize a object (instance of various members of a class).
2. In python there are two types of constructors:

    - parameterized constructor: has pre defined parameters.
    - non-parameterized constructor does not have any parameters.

## `self` parameter

- The self argument refers to the object itself.
- It is a reference to the current instance of the class and is used to access variables that belongs to that object.
- It does no need to be names as `self` but as conventions goes it is genrally named as `self`, though any correct variable name can work here.
- A method can have any number of parameters, but the first parameter will always be the `self` (reference to the object)

## Example of Constructor

```python
    class Student:
        def __init__(self): # Constructor
            pass            
```  

## Creating a method of class

> `method`: It is a python function that is defined inside a class.

### Types of methon

1. Instance mthod
2. Class method
3. Static method
4. Property method (Taught later)

#### 1. Instance method

- The purpose of Instance method is to set or get details about instances (object) that is why they are known as instance method
- They are the most common type of method used ina python class
- Default parameter: `self` - it point to an __object__ (instance of the class)

``` python
    class Example:
        def __init__(self):
            pass

        def instance_method(self):
            return "This is an instance method"

    example_1 = Example()
    example_1.instance_method()
```

> OUTPUT
>
> This is an instance method

``` python
    class Example:
        def __init__(self):
            pass

        def instance_method(self, a):
            return f"This is an instance method with a parameter a = {a}"

    example_1 = Example()
    example_1.instance_method(58)
```

> OUTPUT
>
> This is an instance method with a parameter a = 58

## Decorators in python

Python has an interesting feature called __decorators__ to add functionalty to an existing code.

A python __decorator__ function that takes in a fucntion, added some functionality to it and return the original function.

It works like a wrapper, and when used the function it is used on it passed as a argument. (It works liek a wrapper for a function).

### Prerequisites for learning decorators

1. A function is an instance of a object type.
2. Function can be stored in a variable.
3. Function can be passed as a argument to another function.
4. Function can return a fucntion from a function.
5. Function can be stored in different data structures like list etc.

- [Demonstration of functions as a argument and storign functions as a variable](./decorators/prerequisites/function_as_argument.py)

- [Demonstration of functions inside a funcion](./decorators/prerequisites/function_inside_function.py)

### [Program to demonstrate decorators](./decorators/main.py)

> Q1. Write a decorator functiosn to decorate addition to give factorial

- [Answer 1](./decorators/question_1.py)

> Q2. Write a decorator functiosn to decorate addition to give square

- [Answer 2](./decorators/question_2.py)

#### 2. Class method

Class methods are methods that are called on the class itself not on a specific object instance, and all class instances share a class method.

1. A class method is bound to the class and not to the object of the class, It can access only class variables.
2. It can modify the class state by chnaging the values of the class variable that would apply across all the class objects.

> Q3. Create a Python class names Rectangle constructed by length and width
a. Create a method called area which will compute the area of the rectangle

- [Answer 3](./decorators/question_3.py)