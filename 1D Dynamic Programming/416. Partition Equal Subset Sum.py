# ---------------------- Recursion with Memoization (Top-Down DP) ----------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def dfs(i, current_sum):
            if current_sum == target:
                return True
            if i >= len(nums) or current_sum > target:
                return False
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            include = dfs(i + 1, current_sum + nums[i])
            exclude = dfs(i + 1, current_sum)
            memo[(i, current_sum)] = include or exclude
            return memo[(i, current_sum)]

        return dfs(0, 0)

# ---------------------- Bottom-Up Dynamic Programming (1D DP) ----------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
