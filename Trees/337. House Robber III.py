# ---------------------------- Brute Force Recursion ----------------------------

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        money_with_root = root.val
        if root.left:
            money_with_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money_with_root += self.rob(root.right.left) + self.rob(root.right.right)

        money_without_root = self.rob(root.left) + self.rob(root.right)

        return max(money_with_root, money_without_root)

# ---------------------------- Recursion with Memoization ----------------------------

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            money_with_node = node.val
            if node.left:
                money_with_node += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                money_with_node += dfs(node.right.left) + dfs(node.right.right)

            money_without_node = dfs(node.left) + dfs(node.right)
            memo[node] = max(money_with_node, money_without_node)
            return memo[node]
        return dfs(root)

# ---------------------------- Dynamic Programming Using DFS Returning Two Values ----------------------------

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            rob_current = node.val + left[0] + right[0]
            not_rob_current = max(left) + max(right)
            return (not_rob_current, rob_current)

        return max(dfs(root))