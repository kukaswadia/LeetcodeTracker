# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = {}

        def helper(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            max_sum = 0
            curr_max = 0

            for j in range(i, min(i + k, n)):
                curr_max = max(curr_max, arr[j])
                candidate = curr_max * (j - i + 1) + helper(j + 1)
                max_sum = max(max_sum, candidate)

            memo[i] = max_sum
            return max_sum

        return helper(0)

# ----------------------------- Bottom-Up Dynamic Programming (Iterative) -----------------------------

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            curr_max = 0
            max_sum = 0

            for j in range(i, min(i + k, n)):
                curr_max = max(curr_max, arr[j])
                max_sum = max(max_sum, curr_max * (j - i + 1) + dp[j + 1])
            dp[i] = max_sum
        return dp[0]