# You are given three integers x, y, and z representing the dimensions of a cuboid. You are also given an integer n.

# You need to print a list of all possible coordinates [i, j, k] such that:

# 0 <= i <= x

# 0 <= j <= y

# 0 <= k <= z

# The sum of i + j + k is not equal to n.

# The output list should be printed in lexicographic increasing order.

# Input Format
# x
# y
# z
# n

# Constraints
# 0 <= x, y, z <= 100

# 0 <= n <= x + y + z

# Sample Input
# 1
# 1
# 1
# 2
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [
        [i, j, k] 
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1) 
        if (i + j + k) != n
    ]
    
    print(result)


#     Approach
# Understand the Inputs:
# The program takes four integers as input:
# x: Upper bound for the first coordinate i.
# y: Upper bound for the second coordinate j.
# z: Upper bound for the third coordinate k.
# n: The sum that i + j + k should not equal.
# All inputs are expected to be non-negative integers.
# Generate All Possible Coordinates:
# We need to create all possible combinations of [i, j, k] where:
# i takes values from 0 to x (inclusive, so range(x + 1)).
# j takes values from 0 to y (inclusive, so range(y + 1)).
# k takes values from 0 to z (inclusive, so range(z + 1)).
# This can be thought of as generating points in a 3D grid of size (x+1) × (y+1) × (z+1).
# Filter Coordinates Based on the Condition:
# For each coordinate [i, j, k], compute the sum i + j + k.
# Include only those coordinates where the sum is not equal to n (i.e., i + j + k != n).
# Use List Comprehension for Efficiency:
# Python’s list comprehension allows us to combine the generation and filtering steps concisely.
# The list comprehension will iterate over all possible i, j, and k values and include only those coordinates that satisfy the condition.
# Output the Result:
# Store the valid coordinates in a list and print it as the final output.
# Each coordinate is represented as a list [i, j, k], and the output is a list of such lists.
# Step-by-Step Execution
# Read Inputs: Use input() to read x, y, z, and n, converting each to an integer using int().
# List Comprehension:
# Iterate i from 0 to x using range(x + 1).
# For each i, iterate j from 0 to y using range(y + 1).
# For each j, iterate k from 0 to z using range(z + 1).
# For each combination [i, j, k], check if i + j + k != n.
# If the condition is true, include [i, j, k] in the output list.
# Print the List: Output the resulting list of coordinates.
