s = 'Hello'

# print(s)

x = 5

# print(x)

name = 'Adarsh'
age = 25

# Using format spec... (legacy)
print("%s is %d years old." % (name, age))

# Using .format() method
print("{} is {} years old".format(name, age))

# Using position placeholder for .format() method
print("{0} is {1} years old.".format(name, age))

# Using variable placeholder for .format() method
print("{name_of_person} is {age_of_person} years old.".format(name_of_person=name, age_of_person=age))

# Uaing f-string
print(f"Name: {name}\nAge: {age}")