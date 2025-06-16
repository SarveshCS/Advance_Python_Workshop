def fun(r):
    a = 0
    b = 1

    for _ in range(r):
        c = a
        a = b
        b = c + b
        yield c

a = fun(10)
for i in a:
    print(i)
print()
# One liner

a = {i for i in range(10)}

for i in a:
    print(i)