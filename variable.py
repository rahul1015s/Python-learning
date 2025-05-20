# Variables & Data Types

# Strings (str) - textual data
name_rahul = "rahul"     # Using double quotes
greeting = 'Hello'       # Single quotes also work
multiline = """This is
a multi-line
string"""
print(name_rahul)        # Output: rahul

# Booleans (bool) - True/False values
is_published = True      # Note capital T
is_active = False        # Note capital F
print(is_published)      # Output: True

# Numbers
rating = 4.34            # float (decimal number)
price = 9.99             # another float example
student_count = 1000     # integer (whole number)
negative_num = -15       # integers can be negative

# Type checking
print(type(name_rahul))  # <class 'str'>
print(type(is_published))# <class 'bool'>
print(type(rating))      # <class 'float'>
print(type(student_count))# <class 'int'>

# Type conversion
int_to_float = float(student_count)  # 1000.0
float_to_int = int(rating)           # 4 (truncates decimal)
# Truncates decimal = Cut off the decimal part of a number and keep only the whole number (integer part), without rounding
number_to_str = str(student_count)   # "1000"

# Variable naming conventions:
# - snake_case (recommended in Python)
# - descriptive names
# - case sensitive (Age ≠ age)
# - cannot start with numbers