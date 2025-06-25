# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            best = float('-inf')
            total = 0

            for j in range(1, 4):
                if i + j - 1 < n:
                    total += stoneValue[i + j - 1]
                    best = max(best, total - dfs(i + j))

            memo[i] = best
            return best

        result = dfs(0)
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"

# ----------------------------- Bottom-Up Dynamic Programming (Iterative) -----------------------------

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            for j in range(1, 4):
                if i + j - 1 < n:
                    total += stoneValue[i + j - 1]
                    best = max(best, total - dp[i + j])
            dp[i] = best

        result = dp[0]
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"