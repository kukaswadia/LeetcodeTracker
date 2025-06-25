# ----------------------------- Brute Force Recursion (Backtracking) -----------------------------

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        count = 0
        for num in nums:
            if target - num >= 0:
                count += self.combinationSum4(nums, target - num)
        return count

# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        if target in memo:
            return memo[target]

        if target == 0:
            return 1

        count = 0
        for num in nums:
            if target - num >= 0:
                count += self.combinationSum4(nums, target - num)
        memo[target] = count
        return count

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]