def fact(fun):
    def inner(*arg):
        fact = 1
        res = fun(*arg)
        for i in range(res, 0, -1):
            fact *= i
        return fact
    return inner

@fact
def add(a, b):
    return a + b

print(add(3, 2))