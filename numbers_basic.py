# User Input and Type Conversion
x = input("x: ")  # Input is always string
y = int(x) + 1     # Convert to int for math
print(f"x: {x}, y: {y}")  # f-string formatting

# Falsy Values (Evaluate to False in conditions)
falsey_values = [
    "",     # Empty string
    0,      # Zero integer
    None,   # Absence of value
    False,  # Boolean false
    [],     # Empty list
    {},     # Empty dict,  (short for dictionary) is a collection of key-value pairs
    # A dictionary is like a real dictionary: you look up a word (key) to find its definition (value)
    ()      # Empty tuple , 
    # A tuple is like a sealed box that holds multiple items. Once packed and sealed, you can’t change what's inside
]

# Usage example:
value = 0
if not value:
    print("This is falsy")  # Will execute