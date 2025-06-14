# Chained/Combined Comparisons


# Basic Example (Age Range Check)
age = 25

# Traditional way (without chaining)
if age >= 18 and age < 65:
    print("Traditional: Eligible")

# Pythonic chained comparison
if 18 <= age < 65:
    print("Chained: Eligible")  # Output: "Chained: Eligible"

# =============================
# More Chained Comparison Examples
# =============================

# Temperature range check
temperature = 22
if 20 <= temperature <= 25:
    print("Comfortable temperature")  # Will execute

# Score grading system
score = 85
if 80 <= score < 90:
    print("Grade: B")  # Will execute

# Negative range check
balance = -50
if -100 <= balance < 0:
    print("Warning: Negative balance")

# =============================
# Key Features:
# =============================
# 1. More readable than using 'and'
# 2. Evaluates as (18 <= age) and (age < 65)
# 3. Works with all comparison operators (<, <=, >, >=, ==, !=)
# 4. Can chain multiple comparisons (a < b < c < d)

# Best Practices:
# - Use for range checks
# - Avoid overly long chains (3-4 max)
# - Maintain consistent direction (either all < or all >)

# Note: This is equivalent to mathematical notation
# (e.g., 18 ≤ age < 65)