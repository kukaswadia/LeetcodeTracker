# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def ways(i, rem):
            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0

            if (i, rem) in memo:
                return memo[(i, rem)]

            use_it = ways(i, rem - coins[i])
            skip_it = ways(i + 1, rem)

            memo[(i, rem)] = use_it + skip_it
            return memo[(i, rem)]

        return ways(0, amount)

# ----------------------------- Bottom-Up Dynamic Programming (Iterative) -----------------------------

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]