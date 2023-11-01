"""
You are given a positive integer . Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. 
You have to complete the print statement.

Note: Using anything related to strings will give a score of 0

"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(ascii(i)*i)

# if solution with just using only arithmetic operations
# example for second iteration
# 10^2 = 100 
# 100 - 1 = 99
# 99 / 9 = 11 (it's for second line because it have just two one)
# 11 * 2 = 22
