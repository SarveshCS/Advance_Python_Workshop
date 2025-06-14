class CustomList:
    def __init__(self):
        self._data = []
        self._index = 0
    
    def append(self, item):
        self._data.append(item)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self._data):
            value = self._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration
    
    def remove(self, item):
        self._data.remove(item)
    
    def insert(self, index, item):
        self._data.insert(index, item)
    
    def pop(self, index=-1):
        return self._data.pop(index)
    
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f"CustomList({self._data})"


# ============================
# ITERABLE vs ITERATOR CONCEPTS
# ============================

"""
IMPORTANT CONCEPTS:

1. ITERABLE: An object that can be iterated over (has __iter__ method)
   - Examples: list, tuple, string, dict, set
   - When you call iter() on it, it returns an ITERATOR

2. ITERATOR: An object that represents a stream of data (has both __iter__ and __next__)
   - Has __iter__ method that returns itself
   - Has __next__ method that returns the next item
   - Raises StopIteration when no more items

3. YOUR CustomList is BOTH an iterable AND an iterator (which is unusual!)
   - This can cause problems because it maintains state
"""

print("=" * 60)
print("DEMONSTRATION OF ITERABLE vs ITERATOR")
print("=" * 60)

# Creating our custom list
lst = CustomList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(f"CustomList contents: {lst}")
print()

# ============================
# EXAMINING BUILT-IN LIST (ITERABLE ONLY)
# ============================
print("1. BUILT-IN LIST (Iterable Only):")
print("-" * 40)

regular_list = [1, 2, 3, 4, 5]
print(f"Regular list: {regular_list}")

# Check what methods a regular list has
list_methods = [method for method in dir(regular_list) if method.startswith('__iter__') or method.startswith('__next__')]
print(f"Iterator-related methods in list: {list_methods}")

# A list is iterable but NOT an iterator
print(f"Has __iter__: {'__iter__' in dir(regular_list)}")
print(f"Has __next__: {'__next__' in dir(regular_list)}")

# When we call iter() on a list, it returns a list_iterator
list_iterator = iter(regular_list)
print(f"Type of iter(list): {type(list_iterator)}")
print(f"Iterator methods: {[method for method in dir(list_iterator) if method.startswith('__iter__') or method.startswith('__next__')]}")

print()

# ============================
# EXAMINING YOUR CUSTOM LIST (BOTH ITERABLE AND ITERATOR)
# ============================
print("2. YOUR CUSTOM LIST (Both Iterable AND Iterator):")
print("-" * 50)

print(f"CustomList: {lst}")

# Check what methods your custom list has
custom_methods = [method for method in dir(lst) if method.startswith('__iter__') or method.startswith('__next__')]
print(f"Iterator-related methods in CustomList: {custom_methods}")

# Your CustomList is BOTH iterable AND iterator
print(f"Has __iter__: {'__iter__' in dir(lst)}")
print(f"Has __next__: {'__next__' in dir(lst)}")

# When we call iter() on your CustomList, it returns itself
custom_iterator = iter(lst)
print(f"Type of iter(CustomList): {type(custom_iterator)}")
print(f"iter(lst) is lst: {custom_iterator is lst}")  # True - returns itself!

print()

# ============================
# DEMONSTRATING THE DIFFERENCE IN BEHAVIOR
# ============================
print("3. BEHAVIOR DIFFERENCES:")
print("-" * 30)

print("Regular List - Multiple iterations work fine:")
for i in regular_list:
    print(f"  {i}", end="")
print()
for i in regular_list:  # Works fine - creates new iterator each time
    print(f"  {i}", end="")
print()

print("\nYour CustomList - Problem with multiple iterations:")
print("First iteration:")
for i in lst:
    print(f"  {i}", end="")
print()

print("Second iteration (might not work as expected):")
for i in lst:  # Might not work because iterator state is exhausted
    print(f"  {i}", end="")
print()

print()

# ============================
# BETTER IMPLEMENTATION - SEPARATE ITERATOR CLASS
# ============================
print("4. BETTER IMPLEMENTATION:")
print("-" * 30)

class BetterCustomList:
    """
    This is a better implementation where the list is ONLY iterable,
    and returns a separate iterator object.
    """
    def __init__(self):
        self._data = []
    
    def append(self, item):
        self._data.append(item)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        # Returns a separate iterator object
        return CustomListIterator(self._data)
    
    def __str__(self):
        return str(self._data)

class CustomListIterator:
    """
    Separate iterator class that maintains its own state
    """
    def __init__(self, data):
        self._data = data
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._data):
            value = self._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

# Testing the better implementation
better_list = BetterCustomList()
better_list.append(10)
better_list.append(20)
better_list.append(30)

print(f"BetterCustomList: {better_list}")
print(f"Has __iter__: {'__iter__' in dir(better_list)}")
print(f"Has __next__: {'__next__' in dir(better_list)}")

# Get iterator
better_iterator = iter(better_list)
print(f"Type of iterator: {type(better_iterator)}")
print(f"Iterator has __iter__: {'__iter__' in dir(better_iterator)}")
print(f"Iterator has __next__: {'__next__' in dir(better_iterator)}")

print("\nMultiple iterations work fine with better implementation:")
print("First iteration:")
for item in better_list:
    print(f"  {item}", end="")
print()

print("Second iteration:")
for item in better_list:  # Works perfectly - creates new iterator each time
    print(f"  {item}", end="")
print()

# ============================
# MANUAL ITERATION DEMONSTRATION
# ============================
print("\n5. MANUAL ITERATION:")
print("-" * 25)

print("Manual iteration with built-in list:")
list_iter = iter([1, 2, 3])
try:
    while True:
        print(f"  next(): {next(list_iter)}")
except StopIteration:
    print("  StopIteration raised")

print("\nManual iteration with your CustomList:")
lst._index = 0  # Reset index
try:
    while True:
        print(f"  next(): {next(lst)}")
except StopIteration:
    print("  StopIteration raised")

print("\n" + "=" * 60)
print("SUMMARY:")
print("=" * 60)
print("""
1. Built-in list: ITERABLE only
   - Has __iter__ method
   - iter(list) returns a list_iterator object
   - Can iterate multiple times safely

2. Your CustomList: BOTH iterable AND iterator
   - Has both __iter__ and __next__ methods
   - iter(custom_list) returns itself
   - Problem: Can't iterate multiple times safely

3. Better approach: Separate iterator class
   - List class: Only has __iter__ (iterable)
   - Iterator class: Has both __iter__ and __next__
   - Each iteration creates a new iterator object
""")