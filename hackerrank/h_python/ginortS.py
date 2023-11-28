"""
You are given a string .
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""

input = "Sorting1234"

uppers = []
lowers = []
odds = []
evens = []

for char in input:
    if char.isdigit():
        if int(char) % 2 == 0:
            evens.append(char)
        else:
            odds.append(char)
    else:
        if char.isupper():
            uppers.append(char)
        else:
            lowers.append(char)

letters = sorted(lowers) + sorted(uppers)
digits = sorted(odds) + sorted(evens)
res = letters + digits
print(''.join(res))