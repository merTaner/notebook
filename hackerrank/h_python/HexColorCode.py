"""
- It must start with a '#' symbol.
- It can have 3 or 6 digits.
- Each digit is in the range of 0 to F.
- A-F letters can be lower case.

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
} 

Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
"""

import re

n = int(input())
for _ in range(n) :
    line = input()
    m = re.findall(r"(?:.)(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})(?:\b)", line)
    if m :
        for coincidence in m :
            print(coincidence)
