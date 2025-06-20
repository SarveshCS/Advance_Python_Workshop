class Test:
    def __init__(self, data):
        self._data = data
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, new_data):
        self._data = new_data
        print('Done, data updated!')
        return self._data
    
    @data.deleter
    def data(self):
        raise Exception("Don't delete me I am really important!")
    
test = Test('hehe')

print(test.data)

test.data = 'Yo'

print(test.data)

del test.data
