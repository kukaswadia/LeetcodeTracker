# ---------------------- Top-Down Dynamic Programming (Memoization) ----------------------

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(index):
            if index == len(s):
                return 1

            if s[index] == "0":
                return 0

            if index in memo:
                return memo[index]

            count = decode(index + 1)

            if index + 1 < len(s) and 10 <= int(s[index : index + 2]) <= 26:
                count += decode(index + 2)

            memo[index] = count
            return count

        return decode(0)

# ---------------------- Bottom-Up Dynamic Programming ----------------------

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if (i + 1 < n) and (10 <= int(s[i : i + 2]) <= 26):
                    dp[i] += dp[i + 2]

        return dp[0]

