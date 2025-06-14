class Computer:
    def __init__(self):
        self.__max_price = 1000
    
    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price
    
c = Computer()
c.sell()
c.set_max_price(2458)
c.sell()
print(c._Computer__max_price) # Way to access private class variable