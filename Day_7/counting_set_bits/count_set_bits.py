def count_set(n):
    count = 0
    while n:
        count +=  n & 1
        n>>=1

    return count

n = 6
print(count_set(n))