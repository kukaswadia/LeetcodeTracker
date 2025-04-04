# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                memo[(i, j)] = i == len(s)
                return memo[(i, j)]

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                memo[(i, j)] = first_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        return dp(0, 0)

# ------------------- Bottom-Up Dynamic Programming (Tabulation) -------------------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == '.')
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]