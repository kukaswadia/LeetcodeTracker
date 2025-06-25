# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        keys = sorted(counts.keys())
        points = {num: num * counts[num] for num in keys}

        memo = {}

        def dfs(i):
            if i >= len(keys):
                return 0
            if i in memo:
                return memo[i]

            skip = dfs(i + 1)
            take = points[keys[i]]

            if i + 1 < len(keys) and keys[i + 1] == keys[i] + 1:
                take += dfs(i + 2)
            else:
                take += dfs(i + 1)
            result = max(skip, take)

            memo[i] = result
            return result

        return dfs(0)

# ----------------------------- Bottom-Up Dynamic Programming (House Robber Analogy) -----------------------------

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counts = Counter(nums)
        max_val = max(nums)
        points = [0] * (max_val + 1)

        for num, cnt in counts.items():
            points[num] = num * cnt

        dp = [0] * (max_val + 1)
        dp[0] = 0
        dp[1] = points[1]

        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        return dp[max_val]