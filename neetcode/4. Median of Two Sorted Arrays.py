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
    def findMedianSortedArrays_(self, nums1: list[int], nums2: list[int]) -> float:
        # if lenght to sum of those arrays mod %2 == 0 then make stuff
        # else make differente stuff
        
        # Merge the two sorted arrays into one sorted array
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        # Check if the merged array has an odd or even length
        if n % 2 == 1:
            # If it's odd, return the middle element
            return float(merged[n // 2])
        else:
            # If it's even, return the average of the two middle elements
            mid1 = n // 2
            mid2 = mid1 - 1
            return (merged[mid1] + merged[mid2]) / 2.0
        

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Question is want to O(log(n+m)) you should use binary search 
        
        A, B = nums1, nums2

        total_elements = len(nums1) + len(nums2)
        half = total_elements // 2

        # if B is smaller, swap them
        if len(B) < len(A):
            A, B = B, A

        # we are interested in single Binary Search in smaller sequence
        l, r  = 0 , len(A) - 1

        while True:

            # pointer for A
            i = l + ((r - l) // 2) # A
            
            # pointer for B
            # the remainder from the half number for the longer sequence
            # -2 because -1 from both indexes, arrays start from 0
            j = half - i - 2

            # any of i and j can be out of bounds, we need to cover edge cases
            # for exmaple when i < 0

            a_left = A[i] if i >= 0 else float("-infinity")
            a_right = A[i + 1] if (i+1) < len(A) else float("infinity")

            b_left = B[j] if j >= 0 else float("-infinity")
            b_right = B[j + 1] if (j+1) < len(B) else float("infinity")

            # correct partition:
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total_elements % 2: # 1 is True :)
                    return min(a_right, b_right) / 1
                
                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                # we have too many elements form a left
                r = i - 1
            else:
                l = i + 1


    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))
    print(sol.findMedianSortedArrays([1,2], [3,4]))
    print(sol.findMedianSortedArrays([0,0], [0,0]))
    print(sol.findMedianSortedArrays([1,3], [2,7]))
    print(sol.findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1]))