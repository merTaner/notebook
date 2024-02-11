"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8


    
Takeaway:

in each case, we have different case with open parentheses and closed parentheses

it have to be number of open parenthesis equal to close parentgesis
generate is start have to with open parenthesis

it would be close < open parenthesis

only add open parenthesis if open < n

valid if open = n = close
"""

class Solution:
    # neet solution
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append(''.join(stack))
                return
            
            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(')')
                backtrack(open_n, closed_n + 1)
                stack.pop()


        backtrack(0, 0)
        return res

        
                

                












if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(1))
