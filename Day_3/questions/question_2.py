# Question 4 of Workshop pdf


class String:
    def __init__(self, string):
        self.string = string
        self.length = len(self.string)

        self.no_of_uppercase = None
        self.no_of_lowercase = None
        self.no_of_vowels = None
        self.no_of_consonants = None
        self.no_of_spaces = None

    def count_uppercase(self):
        count = 0
        for i in range(self.length):
            if self.string[i].isupper():
                count+=1
        if self.no_of_uppercase is None:
            self.no_of_uppercase = count
        return self.no_of_uppercase
    
    def count_lowercase(self):
        count = 0
        for i in range(self.length):
            if self.string[i].islower():
                count+=1
        if self.no_of_lowercase is None:
            self.no_of_lowercase = count
        return self.no_of_lowercase
    
    def count_vowels(self):
        count = 0
        vowels = 'aeiouAEIOU'
        for i in range(self.length):
            if self.string[i] in vowels:
                count+=1
        if self.no_of_vowels is None:
            self.no_of_vowels = count
        return self.no_of_vowels
    
    def count_consonants(self):
        count = 0
        vowels = 'aeiouAEIOU'
        for i in range(self.length):
            if self.string[i] not in vowels and self.string[i] != ' ':
                count+=1
        if self.no_of_consonants is None:
            self.no_of_consonants = count
        return self.no_of_consonants
    
    def count_spaces(self):
        count = 0
        for i in range(self.length):
            if self.string[i] == ' ':
                count+=1
        if self.no_of_spaces is None:
            self.no_of_spaces = count
        return self.no_of_spaces
    
    def display(self):
        if self.no_of_uppercase is None:
            self.count_uppercase()
        if self.no_of_lowercase is None:
            self.count_lowercase()
        if self.no_of_vowels is None:
            self.count_vowels()
        if self.no_of_consonants is None:
            self.count_consonants()
        if self.no_of_spaces is None:
            self.count_spaces()
        print(f"Nuber of upper case alphabets:", self.no_of_uppercase)
        print(f"Nuber of lower case alphabets:", self.no_of_lowercase)
        print(f"Nuber of vowels alphabets:", self.no_of_vowels)
        print(f"Nuber of consonants alphabets:", self.no_of_consonants)
        print(f"Nuber of spaces alphabets:", self.no_of_spaces)
        print()

st1 = String("My name is Sarvesh Mishra")
st1.display()
st1.display()
st1.display()