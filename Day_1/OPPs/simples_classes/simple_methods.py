class Training:
    subject = "Advamce Python" # Class variable
    def display(self):
        msg = "In class method" # Object variable
        print(msg)

T1 = Training()
print(T1.subject)
T1.display()