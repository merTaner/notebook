"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106


    

"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # not true but sametimes working 
        nums = nums1 + nums2
        l, r = 0, len(nums) - 1
        while l < r:
            #m = (l + r) // 2
            if nums[l] <= nums[r]:
                l += 1
            nums[l], nums[r]= nums[r], nums[l]
        
        return sum(nums) / len(nums)
        





if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))
    print(sol.findMedianSortedArrays([1,2], [3,4]))
    print(sol.findMedianSortedArrays([0,0], [0,0]))
    print(sol.findMedianSortedArrays([1,3], [2,7]))