"""
This challenge is only forPython 2.

input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'


Task

You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

"""

x, k = map(int, input().split())

print(eval(input()) == k)

