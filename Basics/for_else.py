# For-Else Loop 


successful = True  # Change to False to see else clause execute

for number in range(3):
    print(f"Attempt {number + 1}") 
    if successful:
        print("Successful!")
        break  # Exits the loop immediately
else:
    # Only executes if loop completes WITHOUT hitting break
    print("Attempted 3 times and failed")

# ========================
# Key Behaviors:
# ========================
# When successful = True:
# Attempt 1
# Successful!
# (else block SKIPPED)

# When successful = False:
# Attempt 1
# Attempt 2
# Attempt 3
# Attempted 3 times and failed

# ========================
# Common Use Cases:
# ========================
# 1. Search operations (break when found)
# 2. Validation checks (break when valid)
# 3. Retry mechanisms (else for final failure)

# ========================
# Pro Tips:
# ========================
# - The else clause is for loop completion, not conditions
# - Works with while loops too
# - Avoid complex logic in else (keep it simple)