def deco_add(add):
    def square(*arg):
        res = add(*arg)
        return res**2
    return square

@deco_add
def add(a, b):
    return a + b

print(add(3, 2))