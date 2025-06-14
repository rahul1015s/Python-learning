# Nested Loops - Coordinate Grid

for x in range(5):        # Outer loop (rows)
    for y in range(3):    # Inner loop (columns)
        print(f"({x}, {y})", end=' ')  # Same line
    print()               # New line after inner loop completes

# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
# (3, 0) (3, 1) (3, 2)
# (4, 0) (4, 1) (4, 2)

# ========================
# Key Concepts:
# ========================
# 1. Outer loop runs first (x-axis)
# 2. Inner loop completes FULLY for each outer iteration
# 3. Total iterations = outer_range × inner_range (5×3=15)
# 4. print() with end=' ' keeps coordinates on same line
# 5. Empty print() creates row breaks

# ========================
# Practical Applications:
# ========================
# 1. Grid-based systems (games, matrices)
# 2. Generating combinations
# 3. Multi-dimensional data processing

# ========================
# Advanced Example - Multiplication Table
# ========================
print("\nMultiplication Table:")
for i in range(1, 6):       # 1-5
    for j in range(1, 11):   # 1-10
        print(f"{i*j:3}", end=' ')  # Formatted spacing
    print()  # New line after each row

# Formatting Tip: 
# {i*j:3} reserves 3 spaces for alignment