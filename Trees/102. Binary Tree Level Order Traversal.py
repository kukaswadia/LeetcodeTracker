# ------------------------------- Breadth-First Search (BFS) Using a Queue -------------------------------

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)
        return result

# ------------------------------- Depth-First Search (DFS) with Recursion -------------------------------

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, level):
            if not node:
                return

            if len(result) == level:
                result.append([])
            result[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return result
