# ----------------------- Brute Force (Recursive without Memoization) -----------------------

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        trees = []
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes

            left_trees = self.allPossibleFBT(left_nodes)
            right_trees = self.allPossibleFBT(right_nodes)

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees

# ----------------------- Brute Force (Recursive without Memoization) -----------------------

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        if n in memo:
            return memo[n]

        trees = []
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes
            left_trees = self.allPossibleFBT(left_nodes)
            right_trees = self.allPossibleFBT(right_nodes)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    trees.append(root)
        memo[n] = trees
        return trees