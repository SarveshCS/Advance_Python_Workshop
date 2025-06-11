import time
def decorate(fun):
    def inner():
        print('Started...')
        start = time.time()
        c = fun()
        time_taken = time.time() - start
        print(f"[Total time taken to execute: {time_taken:.2f} ms]")
        return c + ' How are you?'
        
    return inner


@decorate
def hello():
    time.sleep(1.2)
    return "Hello!!"

print(hello())