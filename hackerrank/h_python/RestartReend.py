"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task

You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""

import re

S = input()
k = input()

pattern = re.compile(k)
match = pattern.search(S)

if not match: print("(-1, -1)")
while match:
    print(f"({match.start()}, {match.end() - 1})")
    match = pattern.search(S, match.start() + 1)



    

