class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        for ind in range(len(nums)):
            if ind != nums[ind]:
                return ind
        return len(nums)

# O(1) space complexity solution

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return (len(nums) * ((len(nums) + 1)) // 2 - sum(nums))