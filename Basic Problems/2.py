# QUESTION - 
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Output Format

# Print the runner-up score.

# Sample Input

# 5

# 2 3 6 6 5

# Sample Output

# 5


#Approach

# Find the runner-up score:
# 1- Remove duplicates to handle cases where multiple participants have the same score (e.g., multiple maximum scores).
# 2= Sort the unique scores in descending order.
# 3- The runner-up is the second element in this sorted list (index 1), as it’s the score immediately below the maximum.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Remove duplicates by converting to set
    unique_arr = set(arr)
    # Convert back to list and sort in descending order
    sorted_sccore = sorted(unique_arr, reverse=True)
    # The runner-up score is the second element (index 1)
    runner_up = sorted_sccore[1]
    print(runner_up)
    