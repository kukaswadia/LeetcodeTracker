# ------------------------ Recursive Depth-First Search (DFS) ------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(r, curr):
            curr = (curr * 10) + r.val
            if r.left is None and r.right is None:
                self.total += curr
            if r.left:
                dfs(r.left, curr)
            if r.right:
                dfs(r.right, curr)

        dfs(root, 0)
        return self.total


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
