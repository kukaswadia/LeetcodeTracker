# ------------------------- Breadth-First Search (BFS) with a Queue -------------------------
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = level_sum / level_count
            result.append(average)
        return result

# ------------------------- Depth-First Search (DFS) with Recursion -------------------------

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        counts = []

        def dfs(node, level):
            if node is None:
                return

            if level < len(sums):
                sums[level] += node.val
                counts[level] += 1
            else:
                sums.append(node.val)
                counts.append(1)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return [sums[i] / counts[i] for i in range(len(sums))]






















