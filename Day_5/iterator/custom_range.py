class CustomRange:
    def __init__(self, start=0, end=10, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value


for num in CustomRange(1, 6):
    print(num)