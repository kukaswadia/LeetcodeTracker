# ----------------------------- Brute Force (Recursive Backtracking) -----------------------------

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x : x[0])
        n = len(jobs)

        def dfs(i):
            if i >= n:
                return 0

            option1 = dfs(i + 1)
            next_index = i + 1
            while next_index < n and jobs[next_index][0] < jobs[i][1]:
                next_index += 1
            option2 = jobs[i][2] + dfs(next_index)

            return max(option1, option2)

        return dfs(0)

# ----------------------------- Top-Down Dynamic Programming (Memoization) with Binary Search -----------------------------

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x : x[0])
        n = len(jobs)
        start_times = [job[0] for job in jobs]
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            option1 = dp(i + 1)
            next_index = bisect_left(start_times, jobs[i][1])
            option2 = jobs[i][2] + dp(next_index)
            memo[i] = max(option1, option2)
            return memo[i]

        return dp(0)

# ----------------------------- Bottom-Up Dynamic Programming with Binary Search -----------------------------

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x : x[0])
        n = len(jobs)
        start_times = [job[0] for job in jobs]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            next_index = bisect_left(start_times, jobs[i][1])
            take_profit = jobs[i][2] + dp[next_index]
            skip_profit = dp[i + 1]
            dp[i] = max(take_profit, skip_profit)

        return dp[0]
