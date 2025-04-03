# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i + 1, j + 1)
            else:
                replace = 1 + helper(i + 1, j + 1)
                insert = 1 + helper(i, j + 1)
                delete = 1 + helper(i + 1, j)
                memo[(i, j)] = min(replace, insert, delete)
            return memo[(i, j)]

        return helper(0, 0)

# ------------------- Bottom-Up Dynamic Programming (Tabulation) -------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]

# ------------------- Space-Optimized Bottom-Up DP -------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))

        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j - 1], curr[j - 1], prev[j])
            prev = curr
        return prev[n]


