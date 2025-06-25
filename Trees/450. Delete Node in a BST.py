# ------------------------------ Recursive Deletion ------------------------------
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            successor = root.right
            while successor.left:
                successor = successor.left

            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

# ------------------------------ Iterative Deletion ------------------------------

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return root

        if curr.left and curr.right:
            successor_parent = curr
            successor = curr.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            curr.val = successor.val
            parent = successor_parent
            curr = successor

        child = curr.left if curr.left else curr.right

        if parent is None:
            return child

        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

        return root