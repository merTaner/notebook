"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False
"""

from sys import exit

A = set(map(int, input().split()))

for number_of_iteration in range(int(input())):
    other_set = set(map(int, input().split()))
    
    if A.issuperset(other_set) and not A.issubset(other_set):
        continue
    else:
        print(False)
        exit()

print(True)

    

    

    
    