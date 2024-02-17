"""
Given an array of integers heights representing the histogram's bar height where the 
width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4

 

Constraints:

    1 <= heights.length <= 105
    0 <= heights[i] <= 104

    

Forward step : 

look two by two and add result to stack 
look again area is equal to stack value then go at next iteration
if new area greter then stack area so stack is just had to new area 
"""

class Solution:
    def largestRectangleArea_(self, heights: list[int]) -> int:
        stack = [] 

        max_area = 0
        
        for i in range(len(heights) - 1, -1, -1):
            if len(heights) <= 1:
                return heights[0]
            
            total_width = 2
            min_number = min(heights[i], heights[i - 1])
            max_area = max((min_number * total_width), max_area)
            
            if stack and stack[-1] < max_area:
                stack.append(max_area)
            elif stack[-1] > max_area:
                continue
            else:
                total_width += 1
                max_area = min_number * total_width
                stack.pop()
                stack.append(max_area)
        return max_area
            

    # neet solution
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # pair : (index, height)

        for i, h in enumerate(heights):
            # we need two different variable be equal to index
            # one : i
            # onather one : start
            start = i
            # control to last value of stack greater then h
            # if so, pop the value from stack 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # we need continue together with last index
                start = index 
            stack.append((start, h))

        # update to max_area
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
        





if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))
    #print(sol.largestRectangleArea([2,4]))