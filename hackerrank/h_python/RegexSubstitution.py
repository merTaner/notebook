"""
Task

You are given a text of N lines. The text contains && and || symbols.

Your task is to modify those symbols to the following:

&& → and
|| → or

Both && and || should have a space " " on both sides. 
"""

import re 

for _ in range(int(input())):
    print(re.sub(r"(?<=\s)([&|])\1(?=\s)", lambda match: "and" if match.group(0) == "&&" else "or", input()))