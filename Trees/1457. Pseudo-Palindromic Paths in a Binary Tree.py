class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node, mask):
            nonlocal result
            if not node:
                return

            mask ^= (1 << node.val)

            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    result += 1

            else:
                dfs(node.left, mask)
                dfs(node.right, mask)

        dfs(root, 0)
        return result