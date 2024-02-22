"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated 
at an unknown pivot index k (1 <= k < nums.length) such that the 
resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., 
nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104


    
Takeaway:

any time you looking log time complexity, you should look to binary search

at this problem, you have to consider to k would be between 1 <= k <nums.length  

just focus to algorithm
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            k = l + ((r - l) // 2)

            if nums[k] == target:
                return k
            
            # check to left half is sorted
            if nums[l] <= nums[k]:
                # left part is sorted
                if nums[l] <= target < nums[k]:
                    r = k - 1
                else:
                    l = k + 1
            else:
                # right part is sorted
                if nums[k] < target <= nums[r]:
                    l = k + 1
                else:
                    r = k - 1
        
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))
    print(sol.search([4,5,6,7,0,1,2], 3))
    print(sol.search([1], 0))