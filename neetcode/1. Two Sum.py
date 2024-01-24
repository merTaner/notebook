"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_holder = []
        remainder = None
        for idx, value in enumerate(nums):
            # new target digit
            remainder = target - value 

            # now, is new target in nums ?
            if remainder in nums[idx+1:]:
                index_holder.append(nums.index(value))
                index_holder.append(nums.index(remainder, nums.index(value)+1))
                return index_holder
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))