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