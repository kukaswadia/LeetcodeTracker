class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        if not (top <= bottom):
            return False

        middle_row = (top + bottom) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[middle_row][mid]:
                left = mid + 1
            elif target < matrix[middle_row][mid]:
                right = mid - 1
            else:
                return True
        return False