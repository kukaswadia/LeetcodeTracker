# -------------------------------- Recursive Range Check --------------------------------

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, float('-inf'), float('inf'))

# -------------------------------- Recursive Inorder Traversal --------------------------------

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def validate(node):
            if not node:
                return []
            return validate(node.left) + [node.val] + validate(node.right)

        inorder_list = validate(root)

        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i - 1]:
                return False
        return True

# -------------------------------- Iterative Inorder Traversal --------------------------------

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev_val = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            if prev_val is not None and node.val <= prev_val:
                return False

            prev_val = node.val
            root = node.right

        return True