#Printing numbers in a row without using string


# for statement below takes elements starting from 1 to n.

# If you use "in range(n)" it would print the elements starting from 0 to n-1.
# If you use "in range(1,n)" it would print the elements starting from 1 to n-1.
# If you use "in range(1,n+1)" it would print the elements starting from 0 to n. And this is what you want.
# printing without new line requires and addition in print command.

# end = "" would print 123 for example.

# end = " " with 1 space between would print 1 2 3 and so on.
# end = "---" with --- wiuld print 1---2---3---4 and so on.

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')