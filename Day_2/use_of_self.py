# Program to demonstrate use of self

class Food:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color

    def show(self):
        print(f"Fruit is: {self.fruit}\nColor is: {self.color}")

apple = Food('Apple', 'Red')
banana = Food('Banana', "Yellow")
apple.show()
banana.show()