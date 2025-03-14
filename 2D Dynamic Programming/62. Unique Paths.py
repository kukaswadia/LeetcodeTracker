class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(1)
            dp.append(row)

        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]

# ------------------------- Better Optimization -------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp = []
        for i in range(m):
            dp.append(1)

        for row in range(1, n):
            for col in range(1, m):
                dp[col] += dp[col - 1]
        return dp[-1]

# ------------------------- Even Better Optimization -------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1)))
