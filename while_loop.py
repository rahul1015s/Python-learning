# While Loop Examples


# Example 1: 
print("Countdown:")
number = 100
while number > 0:            # Runs until number <= 0
    print(number, end=' ')   # Print on same line
    number //= 2             # Integer division (no decimals)
# Output: 100 50 25 12 6 3 1

# Example 2: User Input Echo (Case-Insensitive Quit)
print("\n\nType messages ('quit' to exit):")
command = ""
while command.lower() != "quit":  # Case-insensitive check
    command = input("> ")         # Get user input
    if command.lower() != "quit": # Avoid echoing "quit"
        print("ECHO:", command)   # Repeat input

# Example Session:
# > Hello
# ECHO: Hello
# > Python
# ECHO: Python
# > QUIT
# (Program exits)