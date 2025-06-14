# Method overloading in Python
# Python doesn't support true method overloading like Java/C++
# But we can simulate it using default parameters or *args

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
    # Another way using *args
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

calc = Calculator()

print(calc.add(5))        # 5
print(calc.add(5, 3))     # 8
print(calc.add(5, 3, 2))  # 10

print(calc.multiply(2))        # 2
print(calc.multiply(2, 3))     # 6
print(calc.multiply(2, 3, 4))  # 24

# Example 2: Using different parameter types
class Display:
    def show(self, data):
        if isinstance(data, str):
            print(f"String: {data}")
        elif isinstance(data, int):
            print(f"Integer: {data}")
        elif isinstance(data, list):
            print(f"List: {data}")
        else:
            print(f"Unknown type: {data}")

display = Display()
display.show("Hello")
display.show(42)
display.show([1, 2, 3])
