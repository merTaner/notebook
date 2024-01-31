"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Takeaway :

use lower() method for lowercase letters

use regex for remove non-alphanumeric characters.

greate strings method : 
str.isalnum(), filter(), lower()

"""

import re

class Solution:
    def isPalindrome_first_solution(self, s: str) -> bool:
        
        new_str = ''

        for c in s.lower():
            if c.isalnum():
                new_str += c

        return new_str[::] == new_str[:: -1]

    def second_solution_palindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        return s[::] == s[:: -1]
    
    def two_pointer_solution():
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.second_solution_palindrome("A man, a plan, a canal: Panama"))
    #print(sol.isPalindrome_first_solution("race a car"))
    #print(sol.isPalindrome_first_solution(" "))
    #print(sol.isPalindrome_first_solution("ab_a"))
    print(sol.second_solution_palindrome("ab_a"))