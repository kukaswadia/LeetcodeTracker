class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def check(row, col, ocean):
            ocean[row][col] = True
            lst = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in lst:
                if r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0]) and not ocean[r][c] and heights[r][
                    c] >= heights[row][col]:
                    check(r, c, ocean)
            return

        result = []
        rows, cols = len(heights), len(heights[0])
        pac = [[False for i in range(cols)] for j in range(rows)]
        atl = [[False for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            check(i, 0, pac)
            check(i, cols - 1, atl)

        for i in range(cols):
            check(0, i, pac)
            check(rows - 1, i, atl)

        for r in range(rows):
            for c in range(cols):
                if atl[r][c] and pac[r][c]:
                    result.append([r, c])

        return result