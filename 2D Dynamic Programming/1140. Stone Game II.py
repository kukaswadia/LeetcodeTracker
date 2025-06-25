# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i >= n:
                return 0
            if (i, m) in memo:
                return memo[(i, m)]

            best = 0
            for x in range(1, min(2 * m, n - i) + 1):
                best = max(best, suffix[i] - dp(i + x, max(m, x)))

            memo[(i, m)] = best
            return best

        return dp(0, 1)