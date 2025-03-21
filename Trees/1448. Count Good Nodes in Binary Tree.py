# ---------------------------------- Optimized Depth-First Search (DFS) – Recursive ----------------------------------

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if not node:
                return 0

            count = 1 if node.val >= current_max else 0
            new_max = max(current_max, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        return dfs(root, root.val)

# ---------------------------------- Breadth-First Search (BFS) – Iterative ----------------------------------

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = deque([(root, root.val)])

        while queue:
            node, current_max = queue.popleft()
            if node.val >= current_max:
                count += 1

            new_max = max(current_max, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return count

