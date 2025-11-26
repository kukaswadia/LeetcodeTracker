class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        triangle = [[1]]     # First row is always [1]
        for i in range(1, numRows):
            row = [1]       # Each row starts with 1
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)   # Each row ends with 1
            triangle.append(row)

        return triangle