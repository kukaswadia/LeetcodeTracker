# Recursive

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)

        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

# Iterative

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left

        curr = root
        while curr:
            while curr.left and curr.left.val < low:
                curr.left = curr.left.right
            curr = curr.left

        curr = root
        while curr:
            while curr.right and curr.right.val > high:
                curr.right = curr.right.left
            curr = curr.right

        return root