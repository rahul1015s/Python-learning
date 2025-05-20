# Logical Operators


# Boolean flags
high_income = True 
good_credit = False
student = False 

# AND operator (both conditions must be True)
if high_income and good_credit:
    print("AND: Eligible")      # Won't execute
else:
    print("AND: Not Eligible")  # Output: "AND: Not Eligible"

# OR operator (at least one condition must be True)
if high_income or good_credit:
    print("OR: Eligible")       # Output: "OR: Eligible"
else:
    print("OR: Not Eligible")

# NOT operator (inverts the boolean)
if not student:
    print("NOT: Eligible")      # Output: "NOT: Eligible"
else:
    print("NOT: Not Eligible")

# Combined operators
if (high_income or good_credit) and not student:
    print("COMBINED: Eligible")  # Output: "COMBINED: Eligible"
else:
    print("COMBINED: Not Eligible")

# ========================
# Key Concepts:
# ========================
# 1. and - Both conditions must be True
# 2. or - At least one condition must be True
# 3. not - Inverts the boolean value
# 4. Parentheses control evaluation order
# 5. Can combine multiple operators

# Truth Table Shortcut:
# and: All must be True
# or: At least one True
# not: Flips True ↔ False

# Practical Applications:
# - Eligibility checks
# - Feature flags
# - Conditional logic flows
