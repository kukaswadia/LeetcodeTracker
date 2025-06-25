# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            if index == len(nums):
                return 1 if current_sum == target else 0
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]

        return dfs(0, 0)

# ----------------------------- Dynamic Programming (Subset Sum Transformation) -----------------------------


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (target + total) % 2 == 1:
            return 0

        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_sum]