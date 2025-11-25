class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0
        rows = defaultdict(int)
        for row in grid:
            # Converts the row to a tuple so it can be used as a dictionary key & increment its count in rows
            rows[tuple(row)] += 1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            pairs += rows[column]
        return pairs

# -------------------------

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = {}

        for row in grid:
            row_str = ','.join(map(str, row))
            row_map[row_str] = row_map.get(row_str, 0) + 1

        count = 0

        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            col_str = ','.join(map(str, col))
            count += row_map.get(col_str, 0)

        return count
        
