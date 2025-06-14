high_income = True 
good_credit = False
student = False 

# ===============================================
# AND Operator Short-Circuiting
# ===============================================
# AND stops evaluating at first False
if high_income and good_credit:  # Python evaluates left-to-right
    # 1. Checks high_income (True) → continues
    # 2. Checks good_credit (False) → STOPS HERE
    # Never reaches the print statement
    print("AND: Eligible")      
else:
    print("AND: Not Eligible")  # Output: "AND: Not Eligible"

# ===============================================
# OR Operator Short-Circuiting (for comparison)
# ===============================================
if high_income or good_credit:  # OR stops at first True
    # 1. Checks high_income (True) → STOPS HERE
    # Never checks good_credit
    print("OR: Eligible")  # Output: "OR: Eligible"

# ===============================================
# Why Short-Circuiting Matters
# ===============================================
# 1. Prevents unnecessary computations
# 2. Avoids potential errors (e.g., checking x before x[0])
# 3. Enables Python idioms like:
#    - user.is_authenticated and user.has_permission
#    - config or load_default_config()

# Practical Example:
# if student and student.grades:  # Safe attribute access
#     print(student.grades)  # Only runs if student exists
