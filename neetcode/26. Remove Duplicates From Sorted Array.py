class Solution:
    def removeDuplicates_(self, nums: list[int]) -> int:
        # not in place solution
        # it's a brute force
        copy_nums = nums.copy()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                copy_nums.remove(nums[i])
        return  copy_nums

    def removeDuplicates(self, nums: list[int]) -> int:
        # list is a mutable
        # for in place result
        # use nums[i] = in place
        # and use two pointer for control to left and right side
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l





sol = Solution()
print(sol.removeDuplicates_(nums=[1,1,2]))
print(sol.removeDuplicates_(nums=[0,0,1,1,1,2,2,3,3,4]))

print()

print(sol.removeDuplicates(nums=[1,1,2]))
print(sol.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))