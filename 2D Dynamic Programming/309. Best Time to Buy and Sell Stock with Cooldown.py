# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if not holding:
                buy = -prices[i] + helper(i + 1, True)
                skip = helper(i + 1, False)
                memo[(i, holding)] = max(buy, skip)

            else:
                sell = prices[i] + helper(i + 2, False)
                hold = helper(i + 1, True)
                memo[(i, holding)] = max(sell, hold)

            return memo[(i, holding)]

        return helper(0, False)

# ----------------------------- Bottom-Up Dynamic Programming (Iterative) -----------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        s0 = 0
        s1 = -prices[0]
        s2 = float('-inf')
        for i in range(1, n):
            prev_s0 = s0
            s0 = max(s0, s2)
            s1 = max(s1, prev_s0 - prices[i])
            s2 = s1 + prices[i]
        return max(s0, s2)