def inc(x):
    return x+1

def operate(fun, x):
    result = fun(x)
    return result

print(operate(inc, 5)) # Output: 6