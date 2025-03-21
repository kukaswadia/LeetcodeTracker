# --------------------------- BFS with Indexing (Queue-based) -----------------------------

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 1)])

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if i == level_length - 1:
                    current_width = index - first_index + 1
                    max_width = max(max_width, current_width)

                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))

        return max_width

# --------------------------- DFS with Recursion -----------------------------

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        first_index = {}

        def dfs(node, index, level):
            if not node:
                return 0

            if level not in first_index:
                first_index[level] = index

            current_width = index - first_index[level] + 1

            left_width = dfs(node.left, index * 2, level + 1)
            right_width = dfs(node.right, index * 2 + 1, level + 1)

            return max(current_width, left_width, right_width)

        return dfs(root, 1, 0)
