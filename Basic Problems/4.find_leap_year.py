#  find if a year is a leap year in Python

# --->  Logic 

#  a year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400

year = int(input("Enter a Number : "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#//// /////////////////////
#/// for HackerRank //////
# ///////////////////////


def is_leap(year):
    leap = False
    
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
    
    
    
    return leap

year = int(input())
print(is_leap(year))