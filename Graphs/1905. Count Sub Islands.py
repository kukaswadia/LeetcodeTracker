class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        sub_count = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0:
                return True
            if grid1[r][c] == 1:
                valid = True
            else:
                valid = False
            grid2[r][c] = 0

            lst = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for dr, dc in lst:
                result = dfs(dr, dc)
                if result == False:
                    valid = False

            return valid

        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_count += 1
        return sub_count
