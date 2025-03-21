# ------------------------- Level Order Traversal (BFS) Approach -------------------------

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        encountered_none = False

        while queue:
            node = queue.pop(0)

            if node is None:
                encountered_none = True
            else:
                if encountered_none:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True

# ------------------------- DFS with Node Indexing Approach -------------------------

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, index):
            if not node:
                return 0, 0

            left_count, left_max = dfs(node.left, 2 * index)
            right_count, right_max = dfs(node.right, 2 * index + 1)

            total_count = 1 + left_count + right_count
            current_max = max(index, left_max, right_max)
            return total_count, current_max

        total_count, max_index = dfs(root, 1)
        return total_count == max_index