class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]

        for index, num in enumerate(nums[1:], start=1):
            max_current = max(num, max_current + num)

            if max_current > max_global:
                max_global = max_current

        return max_global