"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


    
Takeaway ->

firstly i should use set() beacuse don't need to repeat numbers

sorted and then if next elemen - current element = 1 contuie (it's bad idea)

if i go to from reverse of the list can find solution with more few step (not working beacuse it's be the big o(n^2))
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # don't need repeat numbers
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                lenght = 0
                while (n + lenght) in num_set:
                    lenght += 1
                longest = max(lenght, longest)

        return longest
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([0]))