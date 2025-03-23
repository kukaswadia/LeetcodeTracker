class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(num):
            r = n - 1 - (num - 1) // n
            c = (num - 1) % n if (n - r) % 2 == 1 else n - 1 - (num - 1) % n
            return r, c

        q = deque([(1, 0)])
        visited = set()
        visited.add(1)

        while q:
            square, moves = q.popleft()
            if square == n * n:
                return moves

            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    break
                r, c = get_coordinates(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))

        return -1