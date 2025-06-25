# ----------------- Recursive DFS (Brute Force) -----------------

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        new_target = targetSum - root.val
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)

# ----------------- Iterative DFS (Using a Stack) -----------------

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, targetSum)]
        while stack:
            node, curr_sum = stack.pop()
            if node.left is None and node.right is None and node.val == curr_sum:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.val))
            if node.left:
                stack.append((node.left, curr_sum - node.val))
        return False

# ----------------- Breadth-First Search (BFS using a Queue) -----------------

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        queue = deque([(root, targetSum)])
        while queue:
            node, curr_sum = queue.popleft()

            if node.left is None and node.right is None and node.val == curr_sum:
                return True
            if node.left:
                queue.append((node.left, curr_sum - node.val))
            if node.right:
                queue.append((node.right, curr_sum - node.val))

        return False