# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num in memo:
                return memo[num]

            if num == 1:
                return 1
            max_product = 0
            for i in range(1, num):
                product1 = i * (num - i)
                product2 = i * dfs(num - i)
                max_product = max(max_product, product1, product2)

            memo[num] = max_product
            return max_product
        return dfs(n)

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                product1 = j * (i - j)
                product2 = j * dp[i - j]
                dp[i] = max(dp[i], product1, product2)

        return dp[n]