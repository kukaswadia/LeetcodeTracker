# ---------------------- Recursion with Memoization (Divide & Conquer) ----------------------

class Solution:
    def rob_recursive(self, nums):
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            rob_current = nums[i] + dp(i + 2)
            skip_current = dp(i + 1)
            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return dp(0)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        case1 = self.rob_recursive(nums[:-1])
        case2 = self.rob_recursive(nums[1:])

        return max(case1, case2)

# ---------------------- Iterative Dynamic Programming (Bottom-Up) ----------------------

class Solution:
    def rob_iterative(self, nums):
        prev = 0
        curr = 0
        for num in nums:
            new_curr = max(curr, prev + num)
            prev = curr
            curr = new_curr
        return curr

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        case1 = self.rob_iterative(nums[:-1])
        case2 = self.rob_iterative(nums[1:])

        return max(case1, case2)