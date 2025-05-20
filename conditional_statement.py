# Conditional Statements


# Example 1: Standard if-elif-else
temperature = 40 

if temperature > 35:
    print("It's warm")    # Executes if temp > 35
    print("Drink water")  # Multiple statements in block
elif temperature < 24:    # Else-if for another condition
    print("It's nice")    # Executes if temp < 24
else:                     # All other cases
    print("It's cold")    # Executes if 24 <= temp <= 35

print("Done")  # Always executes (outside if-else block)

# ========================
# Ternary Operator (Conditional Expression)
# ========================

# Syntax: 
# value_if_true if condition else value_if_false

# Example 2: Simple eligibility check
age = 19
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)  # Output: "Eligible"

# Example 3: Inline calculation
score = 85
result = "Pass" if score >= 50 else "Fail"
print(f"Result: {result}")  # Output: "Result: Pass"

# Example 4: Nested ternary (avoid overusing!)
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
print(f"Grade: {grade}")  # Output: "Grade: B"

# ========================
# Key Concepts:
# ========================
# Standard Conditionals:
# 1. Use for multiple statements/complex logic
# 2. Indentation defines code blocks
# 3. elif for additional conditions

# Ternary Operator:
# 1. Single-line conditional assignments
# 2. Returns one of two values
# 3. More readable than if-else for simple cases
# 4. Don't nest too deeply (hurts readability)

# Best Practice:
# - Use standard if-elif-else for complex logic
# - Use ternary only for simple true/false assignments