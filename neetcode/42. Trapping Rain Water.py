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

input : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

maxleft : 0 0 1 1 2 2 2 2 3 3 3 3
maxright: 3 3 3 3 3 3 3 2 2 2 1 0
min(l, r):0 0 1 1 2 2 2 2 2 2 1 0
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
        
        if not height: return 0

        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_soluition([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.first_soluition([4,2,0,3,2,5]))
