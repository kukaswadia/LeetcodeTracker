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
    
"""

Important notes:
- for i in range(1, numRows):
    row = [1]  # Each row starts with 1
    
    # Calculate middle elements
    for j in range(1, i):
    
Understanding i - The Row Number:
for i in range(1, numRows): means we're building rows starting from row 1 (since row 0 is already created as [[1]]).

i represents which row we're currently building
range(1, numRows) generates: 1, 2, 3, ..., numRows-1

for j in range(1, i): creates the middle elements of row i.

j represents the position/index in the new row where we're adding elements
range(1, i) -> It runs from 1 to i-1

Why range(1, i)?

- The Pattern:

Row i has i+1 total elements
After placing the starting 1, we need i-1 middle elements
Then we add the ending 1
Total: 1 + (i-1) + 1 = i+1 elements 

So range(1, i) gives us exactly the right number of iterations to fill in all the middle elements!
    
    
"""

