class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        start = "0000"

        if start in dead_set:
            return -1
        queue = deque([(start, 0)])
        visited = set([start])

        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i + 1:]
                    neighbors.append(new_state)
            return neighbors

        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves

            for neighbor in get_neighbors(state):
                if neighbor not in visited and neighbor not in dead_set:
                    visited.add(neighbor)
                    queue.append((neighbor, moves + 1))

        return -1