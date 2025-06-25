# ----------------------------- Dynamic Programming (Subset Sum Method) -----------------------------

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s

# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = {}

        def dfs(i, diff):
            if i == n:
                return abs(diff)
            if (i, diff) in memo:
                return memo[(i, diff)]

            option1 = dfs(i + 1, diff + stones[i])
            option2 = dfs(i + 1, diff - stones[i])
            result = min(option1, option2)
            memo[(i, diff)] = result
            return result

        return dfs(0, 0)