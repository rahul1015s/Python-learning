# Types of Functions 

# Type 1: Perform a Task (No Return)
def greet(name):
    """Prints a greeting message"""
    print(f"Hi {name}")

greet("Rahul")  # Output: Hi Rahul
# Returns None (implicitly)

# Type 2: Return a Value
def get_greeting(name):
    """Returns a greeting string"""
    return f"Hi {name}"

message = get_greeting("Rahul")
print(message)  # Output: Hi Rahul

# Practical use - save to file:
with open("content.txt", "w") as file:
    file.write(message)

# Type 3: With Default Parameters
def increment(number, by=1):
    """Increments number by specified value (default: 1)"""
    return number + by

print(increment(2))    # Output: 3 (uses default)
print(increment(2, 5)) # Output: 7

# =============================================
# Key Concepts:
# =============================================
# 1. Void Functions:
#    - Perform actions without returning values
#    - Implicitly return None

# 2. Value-Returning Functions:
#    - Use 'return' statement
#    - Can assign result to variables
#    - Enable function composition

# 3. Parameter Variations:
#    - Default parameters (by=1)
#    - Can be overridden when calling

