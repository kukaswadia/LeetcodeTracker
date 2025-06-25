class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = min_value = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_value, min_value = min_value, max_value

            max_value = max(num, max_value * num)
            min_value = min(num, min_value * num)
            result = max(result, max_value)

        return result