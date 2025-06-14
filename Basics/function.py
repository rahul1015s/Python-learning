# Functions 


def greet(first_name, last_name):

    """
    Parameters:
        first_name (str): The person's first name
        last_name (str): The person's last name
        
    Returns:
        None: This function only prints output
"""

    print(f"Hi {first_name} {last_name}")
    print("Welcome to this class")



# Function call with positional arguments
greet("Rahul", "Verma")

# =============================================
# Key Concepts Demonstrated:
# =============================================
# 1. Function Definition:
#    - def keyword
#    - Descriptive name (greet)
#    - Parameters in parentheses

# 2. Function Call:
#    - Passing arguments by position
#    - Arguments match parameters in order

# =============================================
# Expected Output:
# =============================================
# Hi Rahul Verma
# Welcome to this class

# =============================================
# Best Practices:
# =============================================
# 1. Use descriptive function names (verbs for actions)
# 2. Document parameters and return values
# 3. Keep functions small/single-purpose
# 4. Use type hints in modern Python 