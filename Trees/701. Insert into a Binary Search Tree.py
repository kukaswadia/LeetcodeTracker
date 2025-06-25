# ------------------------- Recursive Insertion -------------------------
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# ------------------------- Iterative Insertion -------------------------
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        curr = root
        while curr:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root