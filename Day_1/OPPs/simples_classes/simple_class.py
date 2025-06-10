class Greetings:
    message = "Hello OOPs world"

print(Greetings.message)  # This is a class variable so it is not required to create abject to acces this variable

# Though we can create a object and the access the variable
greet = Greetings()
print(greet.message)