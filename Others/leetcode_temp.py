class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return nums, len(nums)


solution = Solution()
a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
b, len = solution.removeDuplicates(a)
print(b)
print(len)