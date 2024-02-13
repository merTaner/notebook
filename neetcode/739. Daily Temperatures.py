"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to 
get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100


    

Takeaway :

days is be index, temperatures is be [index]
so we don't sorted.

if day < next_day : res[day] += 1
and pop to day from stack
else so day > next_day : top to day from stack and res[day] += 1 

but we need to reverse of stack because it work only this time 


"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures): 
            while stack and stack[-1] < temp:
                res[idx - 1] += 1
                stack.pop()
            stack.append(temp)


                
            
            


        

            

        








if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))

        