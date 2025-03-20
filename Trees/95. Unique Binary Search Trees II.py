# ---------------------- Recursive Divide & Conquer (Brute Force) ----------------------

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def generate_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees

        return generate_trees(1, n)

# ---------------------- Recursive with Memoization ----------------------

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        memo = {}

        def generate_trees(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo [(start, end)]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            memo[(start, end)] = all_trees
            return all_trees

        return generate_trees(1, n)