class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def check(row, col):
            if board[row][col] != "O":
                return
            board[row][col] = "T"
            lst = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for r, c in lst:
                if 0 <= r < ROWS and 0 <= c < COLS:
                    check(r, c)

        for i in range(ROWS):
            if board[i][0] == "O" or board[i][COLS - 1] == "O":
                check(i, 0)
                check(i, COLS - 1)

        for i in range(COLS):
            if board[0][i] == "O" or board[ROWS - 1][i] == "O":
                check(0, i)
                check(ROWS - 1, i)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
