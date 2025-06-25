# ---------------------- Top-Down Dynamic Programming (Memoization) ----------------------

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            rob_current = nums[i] + helper(i + 2)
            skip_current = helper(i + 1)

            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return helper(0)

# ---------------------- Bottom-Up Dynamic Programming (Tabulation) ----------------------

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]

# ---------------------- Bottom-Up Dynamic Programming with Space Optimization ----------------------

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        rob_next = 0
        rob_next_next = 0

        for i in range(n - 1, -1, -1):
            current = max(nums[i] + rob_next_next, rob_next)
            rob_next_next = rob_next
            rob_next = current

        return rob_next