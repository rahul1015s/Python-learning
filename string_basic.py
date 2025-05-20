# String Basics & Slicing
student = "Rahul Verma"
print(student)          # "Rahul Verma"
print(len(student))     # 11 (length includes space)
print(student[0])       # "R" (indexing)
print(student[0:5])     # "Rahul" (slicing first name)
print(student[6:])      # "Verma" (slicing last name)
print(student[:5])      # "Rahul" (from start)
print(student[:])       # "Rahul Verma" (full copy)
print(student[-1])      # "a" (last character)

# Important String Methods
print(student.upper())       # "RAHUL VERMA"
print(student.lower())       # "rahul verma"
print(student.find('V'))     # 6 (index of 'V' in Verma)
print(student.replace('Rahul', 'Rohan'))  # "Rohan Verma"
print('Verma' in student)    # True (substring check)
print(student.split())       # ['Rahul', 'Verma'] (splits at space)
print(student.startswith('Rah'))  # True
print(student.endswith('rma'))    # False (case-sensitive)
print(student.strip())       # removes whitespace (useful if extra spaces)
print(student.isalpha())     # False (contains space)