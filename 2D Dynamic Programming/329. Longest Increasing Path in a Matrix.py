# ------------------- Top-Down Dynamic Programming (Memoization) -------------------

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix and not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            best = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))

            memo[(i, j)] = best
            return best

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result

# ------------------- Topological Sort (BFS Level-Order Traversal) -------------------

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        indegree = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                        indegree[i][j] += 1

        queue = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        longest_path = 0
        while queue:
            longest_path += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))

        return longest_path


