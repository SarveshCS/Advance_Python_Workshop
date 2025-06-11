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
