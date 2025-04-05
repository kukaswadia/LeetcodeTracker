# -------------------------- BFS --------------------------

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] != 0:
                continue
            colors[i] = 1
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

        return True

# -------------------------- DFS --------------------------

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    if not dfs(neighbor, -color):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True

        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
        return True