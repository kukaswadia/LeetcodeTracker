# ------------------- Recursive without memoization -------------------

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1)
            else:
                return max(lcs(i + 1, j), lcs(i, j + 1))

        return lcs(0, 0)

# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

            return memo[(i, j)]

# ------------------- Bottom-Up Dynamic Programming -------------------

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


