"""
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on).
 You are required to sort the data based on the th attribute and print the final resulting table. 
 Follow the example given below for better understanding.

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, 
if two atheletes are of the same age, print the row that appeared first in the input. 

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    for list_items in sorted(arr, key=lambda x: x[k]):
        print(*list_items)
