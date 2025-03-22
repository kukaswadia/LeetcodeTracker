# ---------------------------------- Depth-First Search (DFS) ----------------------------------

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for emp in range(n):
            if manager[emp] != -1:
                children[manager[emp]].append(emp)

        def dfs(current):
            if current not in children:
                return 0

            max_time = 0
            for sub in children[current]:
                time_for_sub = dfs(sub)
                max_time = max(max_time, time_for_sub)

            return informTime[current] + max_time

        return dfs(headID)

# ---------------------------------- Breadth-First Search (BFS) ----------------------------------

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for emp in range(n):
            if manager[emp] != -1:
                children[manager[emp]].append(emp)

        q = deque([(headID, 0)])
        max_time = 0

        while q:
            current, current_time = q.popleft()
            max_time = max(max_time, current_time)
            for subordinate in children[current]:
                q.append((subordinate, current_time + informTime[current]))
        return max_time