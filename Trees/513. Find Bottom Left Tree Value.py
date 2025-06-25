# -------------------------- BFS (Level Order Traversal – Brute Force) --------------------------

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        queue = deque([root])
        bottom_left = root.val

        while queue:
            bottom_left = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottom_left

# -------------------------- DFS Recursive (Preorder Traversal) --------------------------

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bottom_left = root.val
        max_depth = -1

        def dfs(node, depth):
            nonlocal bottom_left, max_depth
            if not node:
                return

            if depth > max_depth:
                max_depth = depth
                bottom_left = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return bottom_left

# -------------------------- DFS Iterative (Using a Stack) --------------------------
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        bottom_left = root.val
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if depth > max_depth:
                max_depth = depth
                bottom_left = node.val

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return bottom_left