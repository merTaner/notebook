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
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))




if __name__ == '__main__':
    sol = Solution()
    #print(sol.second_solution_palindrome("A man, a plan, a canal: Panama"))
    #print(sol.isPalindrome_first_solution("race a car"))
    #print(sol.isPalindrome_first_solution(" "))
    #print(sol.isPalindrome_first_solution("ab_a"))
    #print(sol.second_solution_palindrome("ab_a"))
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))