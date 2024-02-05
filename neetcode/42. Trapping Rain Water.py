"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

Takeaway : 


"""

class Solution:
    def first_soluition(self, height: list[int]) -> int:
        # i want make stuff
        # bad solution but think good try
        l, r = 0, len(height) - 1
        rain = 0
        while l < r:
            if height[l] == 0 :
                l += 1
            if height[r] == 0:
                r -= 1

            if l < r:
                rain += height[l]
                l += 1
            elif l > r:
                rain += height[r]
                r -= 1
            else:
                r -= 1

    

    def trap(self, height: list[int]) -> int:
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_soluition([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.first_soluition([4,2,0,3,2,5]))
