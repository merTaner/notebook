"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.



Takeway :

firstly determine to left and right sembols. left = '([{'

then, control to if charter in left/right each item of list
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """ Return True if all delimiters are properly match; False otherwise. """

        left_bracket = '([{'
        right_bracket = ')]}'
        stack = []

        for c in s:
            if c in left_bracket:
                stack.append(c)
            elif c in right_bracket:
                if len(stack) == 0: return False
                if right_bracket.index(c) != left_bracket.index(stack.pop()): return False
            
        return len(stack) == 0

    def grate_way(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False





if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid('()[]{}'))
    print(sol.isValid("(]"))