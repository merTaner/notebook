"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of 
all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
            Bad solution because Big O(n^2)
        """
        product_holder = {}

        for idx, value in enumerate(nums):
            # Create a copy of the list
            product_numbers = nums[:] 

            # Remove the current element from the copy
            product_numbers.pop(idx)  
            product_holder[value] = product_numbers

        product = 1
        for key, value in product_holder.items():
            for number in value:
                product *= number
            
            product_holder[key] = product
            product = 1

        return list(product_holder.values())

    def product_except_self(self, nums: list[int]) -> list[int]:
        """This method basically uses the idea of product of
         all elements to the left and right for every
          element and when we multiplty the results, we
         get product of all elements except index'th element"""
        
        # better than first solution Big O(n)
        
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == '__main__':
    sol = Solution()
    #print(sol.productExceptSelf([1,2,3,4]))
    #print(sol.productExceptSelf([-1,1,0,-3,3]))
    print(sol.product_except_self([1,2,3,4]))
    print(sol.product_except_self([-1,1,0,-3,3]))