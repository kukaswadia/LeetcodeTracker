# ------------------------- Depth-First Search (DFS) with Recursion -------------------------

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result

# ------------------------- Level Order Traversal Breadth-First Search (BFS) with a Queue -------------------------

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        if not root:
            return []

        while queue:
            level_length = len(queue)
            level_max = float('-inf')

            for _ in range(level_length):
                node = queue.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_max)
        return result