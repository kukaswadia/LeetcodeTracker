# ----------------------------- DFS with Global Minimum (Optimized Memory) --------------------------------
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = "~"

        def dfs(node, path):
            nonlocal smallest
            if not node:
                return

            new_path = chr(ord('a') + node.val) + path

            if not node.left and not node.right:
                if new_path < smallest:
                    smallest = new_path
                return

            dfs(node.left, new_path)
            dfs(node.right, new_path)

        dfs(root, "")
        return smallest

# ----------------------------- Iterative DFS using a Stack --------------------------------

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        smallest = "~"
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()
            new_path = chr(ord('a') + node.val) + path

            if not node.left and not node.right:
                smallest = min(smallest, new_path)

            if node.left:
                stack.append((node.left, new_path))
            if node.right:
                stack.append((node.right, new_path))

        return smallest