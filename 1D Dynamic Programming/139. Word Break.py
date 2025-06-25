# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def canBreak(s):
            if s in memo:
                return memo[s]
            if not s:
                return True
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    if canBreak(s[i:]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return canBreak(s)

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]












