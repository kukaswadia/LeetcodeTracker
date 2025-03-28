# ---------------------- Top-Down Dynamic Programming (Memoization) ----------------------

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if (i, j) in memo:
                return memo[(i, j)]

            left_path = dfs(i + 1, j)
            right_path = dfs(i + 1, j + 1)
            memo[(i, j)] = triangle[i][j] + min(left_path, right_path)
            return memo[(i, j)]
        return dfs(0, 0)

# ---------------------- Bottom-Up Dynamic Programming ----------------------

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]