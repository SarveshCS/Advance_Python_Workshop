def greetings(msg):
    x = "Hello"

    def display():
        print(x, msg)
        
    display()

greetings("How are you?")