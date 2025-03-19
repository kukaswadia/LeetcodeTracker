# ------------------------ Recursive Depth-First Search (DFS) ------------------------

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)

            return left_sum + right_sum

        return dfs(root, 0)

# ------------------------ Iterative DFS Using a Stack ------------------------

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_sum = 0
        stack = [(root, root.val)]

        while stack:
            node, current_sum = stack.pop()

            if not node.left and not node.right:
                total_sum += current_sum

            if node.right:
                stack.append((node.right, current_sum * 10 + node.right.val))
            if node.left:
                stack.append((node.left, current_sum * 10 + node.left.val))

        return total_sum

# ------------------------ Breadth-First Search (BFS) Using a Queue ------------------------

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_sum = 0
        queue = deque([(root, root.val)])

        while queue:
            node, current_sum = queue.popleft()

            if not node.left and not node.right:
                total_sum += current_sum

            if node.left:
                queue.append((node.left, current_sum * 10 + node.left.val))

            if node.right:
                queue.append((node.right, current_sum * 10 + node.right.val))

        return total_sum
