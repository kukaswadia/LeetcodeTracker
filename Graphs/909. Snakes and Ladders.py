# ---------------------- Breadth First Search (BFS) ----------------------

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

# ---------------------- Depth First Search (DFS) ----------------------

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        min_moves = inf

        def get_coordinates(num):
            r = n - 1 - (num - 1) // n
            if (n - r) % 2 == 1:
                c = (num - 1) % n
            else:
                c = n - 1 - (num - 1) % n
            return r, c

        memo = {}

        def dfs(square, moves):
            nonlocal min_moves

            if square == target:
                min_moves = min(min_moves, moves)
                return

            if moves >= min_moves:
                return

            if square in memo and memo[square] <= moves:
                return
            memo[square] = moves

            for i in range(1, 7):
                next_square = square + i
                if next_square > target:
                    continue
                r, c = get_coordinates(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]
                dfs(next_square, moves + 1)

        dfs(1, 0)
        return min_moves if min_moves != inf else -1

# ---------------------- Dijkstra’s Algorithm ----------------------

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        def get_coordinates(num):
            r = n - 1 - (num - 1) // n
            if (n - r) % 2 == 1:
                c = (num - 1) % n
            else:
                c = n - 1 - (num - 1) % n
            return r, c

        heap = [(0, 1)]
        visited = {}

        while heap:
            moves, square = heapq.heappop(heap)
            if square == target:
                return moves
            if square in visited and visited[square] <= moves:
                continue
            visited[square] = moves

            for i in range(1, 7):
                next_square = square + i
                if next_square > target:
                    continue
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited or moves + 1 < visited.get(next_square, inf):
                    heapq.heappush(heap, (moves + 1, next_square))

        return -1
















