"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

 

Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


    

Takeaway:

Reverse Polish Notation --> 34-5+ = first 3 - 4 then add with 5

control 3 expression for each step and if be 3th operator apply to the operator
or one by one for each step and if it's be operator this time going to backword [-2] operator [-1] 
and then delete two number from list and continue

use convert string to able apply operator : eval()
"""
import operator

class Solution:
    # IT'S BE REALLY BRUTE FORCE SOLUTION
    # I forget use to stack :/
    def _evalRPN(self, tokens: list[str]) -> int:
        
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        idx = 0
        while idx < len(tokens):
            token = tokens[idx]
            if token in operators:
                first_number = int(tokens[idx - 2]) 
                second_number = int(tokens[idx - 1]) 
                apply_to_operator = int(operators[token](first_number, second_number))

                tokens.pop(idx - 2)
                idx -= 1
                tokens.pop(idx - 1)
                idx -= 1
                tokens.pop(idx)
                tokens.insert(idx, apply_to_operator)
                idx = 0
            else:
                idx += 1
        
            
        return int(tokens[0])



    def evalRPN(self, tokens: list[str]) -> int:
        pass





if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(sol.evalRPN(['18']))