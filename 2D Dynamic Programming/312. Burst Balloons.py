# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def dp(left, right):
            if left + 1 == right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            max_coins = 0

            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                total = coins + dp(left, i) + dp(i, right)
                max_coins = max(max_coins, total)

            memo[(left, right)] = max_coins
            return max_coins

        return dp(0, n - 1)

# ------------------- Bottom-Up Dynamic Programming (Tabulation) -------------------

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    total = coins + dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], total)

        return dp[0][n - 1]