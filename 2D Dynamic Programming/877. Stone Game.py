# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(l, r):
            if l == r:
                return piles[l]

            if (l, r) in memo:
                return memo[(l, r)]
            left_choice = piles[l] - dfs(l + 1, r)
            right_choice = piles[r] - dfs(l, r - 1)
            memo[(l, r)] = max(left_choice, right_choice)
            return memo[(l, r)]

        return dfs(0, len(piles) - 1) > 0

# ----------------------------- Bottom-Up Dynamic Programming (Iterative) -----------------------------

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

            for length in range(2, n + 1):
                for i in range(n - length + 1):
                    j = i + length - 1
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

            return dp[0][n - 1] > 0