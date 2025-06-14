# For Loop with Range


# Basic range loop with step
for number in range(1, 10, 2):  # start=1, stop=10, step=2
    print("I'm Learning", number, number * ".")

# Output:
# I'm Learning 1 .
# I'm Learning 3 ...
# I'm Learning 5 .....
# I'm Learning 7 .......
# I'm Learning 9 .........

# ========================
# Key Concepts:
# ========================
# range() parameters:
# 1. Start (inclusive, default=0)
# 2. Stop (exclusive)
# 3. Step (increment, default=1)

# String multiplication:
# "." * 3 → "..."

# Alternative formatting (f-strings):
for num in range(1, 10, 2):
    print(f"I'm Learning {num} {'.' * num}")

# Common Patterns:
# 1. range(5)        → 0,1,2,3,4
# 2. range(1, 6)     → 1,2,3,4,5
# 3. range(0, 10, 2) → 0,2,4,6,8

# ========================
# Decrementing Loop Example
# ========================
# Countdown from 5 to 1 using a negative step
for i in range(5, 0, -1):  # start=5, stop=0 (exclusive), step=-1
    print(f"Countdown: {i} {'*' * i}")

# Output:
# Countdown: 5 *****
# Countdown: 4 ****
# Countdown: 3 ***
# Countdown: 2 **
# Countdown: 1 *

# Practical Applications:
# - Generating sequences
# - Repeating operations
# - Progress indicators
# - Countdown timers or reverse patterns
