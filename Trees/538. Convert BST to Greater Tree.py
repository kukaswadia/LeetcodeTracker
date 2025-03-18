# ----------------------------- Reverse In-order Traversal (Recursive) --------------------------------

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def helper(node):
            nonlocal total
            if not node:
                return

            helper(node.right)
            total += node.val
            node.val = total
            helper(node.left)

        helper(root)
        return root

# ----------------------------- Reverse In-order Traversal (Iterative) --------------------------------
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        node = root
        stack = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root