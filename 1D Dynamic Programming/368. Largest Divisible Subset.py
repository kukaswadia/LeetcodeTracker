# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        memo = {}

        def dfs(index, prev_index):
            if index == n:
                return []

            key = (index, prev_index)
            if key in memo:
                return memo[key]
            subset_skip = dfs(index + 1, prev_index)
            subset_take = []
            if prev_index == -1 or nums[index] % nums[prev_index] == 0:
                subset_take = [nums[index]] + dfs(index + 1, index)

            if len(subset_take) > len(subset_skip):
                memo[key] = subset_take
            else:
                memo[key] = subset_skip
            return memo[key]

        return dfs(0, -1)

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > dp[max_index]:
                max_index = i

        subset = []
        while max_index != -1:
            subset.append(nums[max_index])
            max_index = prev[max_index]

        return subset[::-1]