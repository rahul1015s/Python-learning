# Iterables in Python


# Definition:
# An iterable is any object capable of returning its elements one at a time
# Common iterables: lists, strings, tuples, dictionaries, sets, files, generators

# ------------------------
# 1. Basic Iteration Examples
# ------------------------

# String iteration (iterates by character)
word = "hello"
for char in word:
    print(char)  # h, e, l, l, o

# List iteration
numbers = [1, 2, 3]
for num in numbers:
    print(num * 2)  # 2, 4, 6

# Dictionary iteration (by keys by default)
student = {"name": "Rahul", "age": 20}
for key in student:
    print(f"{key}: {student[key]}")  # name: Rahul, age: 20

# ------------------------
# 2. Under the Hood
# ------------------------

# How iteration works:
# 1. iter() calls __iter__() to get an iterator
# 2. next() calls __next__() until StopIteration

# Manual iteration demonstration:
colors = ["red", "green", "blue"]
iterator = iter(colors)  # Get iterator object
print(next(iterator))    # red
print(next(iterator))    # green
print(next(iterator))    # blue
# print(next(iterator))  # Raises StopIteration

# ------------------------
# 3. Common Iterable Operations
# ------------------------

# Membership testing
if "a" in "apple":
    print("Found!")  # Prints

# Unpacking
x, y, z = [10, 20, 30]  # Works with any iterable

# Conversion
unique_chars = set("mississippi")  # {'m', 'i', 's', 'p'}

# ------------------------
# 4. Built-in Functions
# ------------------------

nums = [5, 2, 8, 1]
print(sum(nums))       # 16
print(min(nums))       # 1
print(max(nums))       # 8
print(sorted(nums))    # [1, 2, 5, 8]
print(list(enumerate(nums))) 

# enumerate(nums) returns: [(0, 5), (1, 2), (2, 8), (3, 1)]
# → It pairs each item in the list with its index (position)
# → 0 is the index of 5, 1 is the index of 2, and so on

print(list(enumerate(nums)))  
# Output: [(0, 5), (1, 2), (2, 8), (3, 1)]
# → A list of (index, value) pairs
