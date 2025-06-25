# ------------------------- Brute Force In-order Traversal with a List (Recursion) -------------------------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            elements.append(node.val)
            helper(node.right)

        helper(root)
        return elements[k - 1]

# ------------------------- Recursive In-order Traversal with Early Termination -------------------------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def helper(node):
            nonlocal count, result
            if not node or result is not None:
                return
            helper(node.left)
            count += 1

            if count == k:
                result = node.val
                return

            helper(node.right)
        helper(root)
        return result

# ------------------------- Iterative In-order Traversal using a Stack -------------------------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count +=1

            if count == k:
                return curr.val

            curr = curr.right
        return None


