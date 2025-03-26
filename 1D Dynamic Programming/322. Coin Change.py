# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(remainder):
            if remainder == 0:
                return 0
            if remainder < 0:
                return -1
            if remainder in memo:
                return memo[remainder]

            min_coins = float('inf')
            for coin in coins:
                res = dp(remainder - coin)
                if res >= 0 and res < min_coins:
                    min_coins = res + 1

            memo[remainder] = -1 if min_coins == float('inf') else min_coins
            return memo[remainder]

        return dp(amount)

# ----------------------------- Bottom-Up Dynamic Programming -----------------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1