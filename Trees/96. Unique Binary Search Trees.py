# ------------------------- Recursive Brute Force -------------------------

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        total = 0
        for i in range(1, n + 1):
            left = self.numTrees(i - 1)
            right = self.numTrees(n - i)
            total += left * right
        return total

# ------------------------- Dynamic Programming (Bottom-Up) -------------------------

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = dp[root - 1]
                right = dp[nodes - root]
                total += left * right
            dp[nodes] = total
        return dp[n]

# ------------------------- Mathematical Formula Using Catalan Numbers -------------------------

class Solution:
    def numTrees(self, n: int) -> int:
        catalan = math.comb(2 * n, n) // (n + 1)
        return catalan