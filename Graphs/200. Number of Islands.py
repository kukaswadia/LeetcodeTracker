class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            lst = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
            for row, col in lst:
                if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == '1':
                    dfs(row, col)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands
