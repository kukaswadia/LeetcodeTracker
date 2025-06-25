# DFS Post Order Traversal

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0

            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            moves += abs(left_excess) + abs(right_excess)
            current_excess = node.val + left_excess + right_excess - 1
            return current_excess

        dfs(root)
        return moves