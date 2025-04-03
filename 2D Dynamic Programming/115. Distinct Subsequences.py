# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                memo[(i, j)] = dp(i + 1, j)
            return memo[(i, j)]

        return dp(0, 0)

# ------------------- Bottom-Up Dynamic Programming (Tabulation) -------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]