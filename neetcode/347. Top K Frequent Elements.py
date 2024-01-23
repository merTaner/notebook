"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # frequent numbers 
        frequent_dict = {}

        for number in nums:
            frequent_dict[number] = frequent_dict.get(number, 0) + 1
        
        final_list = [[] for i in range(len(nums) + 1)]

        for key, frequent in frequent_dict.items():
           final_list[frequent].append(key)

            
        result = []
        for i in range(len(final_list) - 1, 0, -1): # it's going from reverse
            for j in final_list[i]:
                result.append(j)

                if len(result) == k:
                    return result
           


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))