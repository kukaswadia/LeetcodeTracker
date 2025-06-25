class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, queue):
            if r < 0 or r >= n or c < 0 or c >= n or visited[r][c] or grid[r][c] != 1:
                return
            visited[r][c] = True
            grid[r][c] = 2
            queue.append((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, queue)

        bfs_queue = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, bfs_queue)
                    found = True
                    break

        steps = 0
        while bfs_queue:
            for _ in range(len(bfs_queue)):
                r, c = bfs_queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if not visited[nr][nc]:
                            if grid[nr][nc] == 1:
                                return steps
                            visited[nr][nc] = True
                            bfs_queue.append((nr, nc))
            steps += 1

        return -1