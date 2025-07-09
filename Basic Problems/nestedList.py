# Question: Find the Students with the Second Lowest Score
# You are given the names and grades of N students. Store them in a list of lists, 
# where each sublist contains a student’s name and grade.
# 
# Your task is to print the names of all students who have the second lowest grade.
# Print their names in alphabetical order, each on a new line.

# ------------------------------------------------------------------------------------
# 🧠 How to Think (Step-by-Step Problem Solving Approach)
# ------------------------------------------------------------------------------------

# 🧩 Step 1: Understand the Problem Clearly
# I am given names and scores of students. 
# I need to find the names of students who have the second lowest score, 
# and print them in alphabetical order.

# 🔍 Step 2: Identify the Inputs and Outputs
# Input:
#   - An integer n — number of students.
#   - For n times:
#       - A string name
#       - A float score
# Output:
#   - Names of students who have the second lowest score,
#     sorted alphabetically, one per line.

# 🧮 Step 3: Break the Problem into Small Tasks

# 1. How can I store names and scores together?
#    => Use a list of lists → [["Rahul", 40.0], ["Sheetal", 50.0], ...]

# 2. How do I find the second lowest score?
#    - Extract all scores into a new list.
#    - Remove duplicates using set.
#    - Sort the scores.
#    - Pick the second lowest score (index 1).

# 3. How do I find which names got that score?
#    - Go back to the original list and collect names where score equals second lowest.

# 4. What if multiple students have the same score?
#    - Sort their names alphabetically.

# 🔧 Step 4: Think in Pythonic Way (Data Structures & Tools)
# - Use list.append() to build the data.
# - Use set() to get unique scores.
# - Use sorted() to sort numbers or strings.
# - Use list comprehensions to filter easily.

# 🗺️ Final Mental Plan:
# 1. Make a list of [name, score] pairs.
# 2. Extract only scores → remove duplicates → sort → get second lowest.
# 3. From the original list, get all names who have that second lowest score.
# 4. Sort those names alphabetically.
# 5. Print them.

# ------------------------------------------------------------------------------------
# 🧠 Summary of the Thinking Pattern 
# ------------------------------------------------------------------------------------
# ✅ Input Parsing  → Use loops and list to collect structured data
# ✅ Filtering       → List comprehension to select based on condition
# ✅ Sorting         → Understand when to sort: scores vs names
# ✅ Duplicates      → Use set() for uniqueness
# ✅ Edge cases      → What if multiple students have same score? Sorted output

# ------------------------------------------------------------------------------------
# 💡 Code 
# ------------------------------------------------------------------------------------

if __name__ == '__main__':
    lst = []  # Step 1: Create an empty list to store [name, score] pairs
    
    # Step 2: Read input (number of students), then each student's name and score
    for _ in range(int(input())):
        name = input()                 # Read student name
        score = float(input())         # Read student score as float
        lst.append([name, score])      # Store both in the list

    # Step 3: Extract all scores using list comprehension
    findScore = [x[1] for x in lst]    # Just take the score from each [name, score]

    # Step 4: Remove duplicates using set(), then sort the scores
    sortScore = sorted(set(findScore))  # Sorted unique scores list

    # Step 5: Get names of students who have the second lowest score
    # sortScore[1] gives second lowest score
    findName = sorted([y[0] for y in lst if(sortScore[1] == y[1])])

    # Step 6: Print names of students with second lowest score in alphabetical order
    for z in findName:
        print(z)
