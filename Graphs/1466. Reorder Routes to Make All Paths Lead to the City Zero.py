# ----------------------------- DFS -----------------------------

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        result = 0
        visited = set()

        def dfs(city):
            nonlocal result
            visited.add(city)
            for neighbour, direction in graph[city]:
                if neighbour not in visited:
                    if direction == 1:
                        result += 1
                    dfs(neighbour)

        dfs(0)
        return result

# ----------------------------- BFS -----------------------------

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        result = 0
        visited = set([0])
        queue = deque([0])

        while queue:
            city = queue.popleft()
            for neighbour, direction in graph[city]:
                if neighbour not in visited:
                    if direction == 1:
                        result += 1
                    visited.add(neighbour)
                    queue.append(neighbour)

        return result