def custom_for_loop(iterable, action):
    iterator = iter(iterable)
    while True:
        try: action(next(iterator))
        except StopIteration: break

a = [1, 2, 3, 4, 5, 6]
custom_for_loop(a, print)