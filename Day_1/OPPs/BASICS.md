# OOP : Object-Oriented Programming

## Topics to cover

- object
- class
- userdefined class
- class variables
- class method
- instance variable
- instance method
- static method
- constructors (`__init__`)
- parameterized constructor

### Object

It is a runtime entity of a class.

It can also be said, that __object is an instance of a class__.

It is a memory reference where properties related to object are kept.

An object consists of `state`, `behaviour` and `identity`.

- State: Attributes of and object
- Behaviour: Methods of an object
- Identity: It gives and Unique name to the object

### Class

Blueprint of a object

### Class variables and objec tvariables

A class can have variables defined in it, these variables are of two types - `class variable` and `object variable`

Class variables are owned by class, Object variables are owned by each object.

#### Object variable

1. If a class has `n` objects then there will be `n` seperate copies of the object variable, as each object will have it's own object variable.

2. The object variable is not shared between objects.

3. A chnage made tot he object variable by one object will not be reflected in the other objects.

#### Class variable

1. If a class have one class variable then there will be one copy only for that variable,
all the objects of that class will share the same class variable.

2. Since there exixts a single copy of the class variable,
any chnages made to the class variable by any object will be reflected in all other objects.

### __init__() method

init means Initialize

it is a magic method (dunder - double underscore)

It is a constructor, and initializes the object (variables of class - to create object).

All classes have this `__init__` method, which is executed when a new object is created using that class.

Use the init method to asign values to object propertiesor other operatiosn that are neccessary to do for creation of a object of tht class.

The init method is called automatically everytime a class is being used to create a new object.

#### self parameter
