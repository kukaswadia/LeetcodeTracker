class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area_islands = 0

        def dfs(r, c):
            num = 1
            grid[r][c] = 0
            lst = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for row, col in lst:
                if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                    num += dfs(row, col)
            return num

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, dfs(r, c))
        return area_islands
