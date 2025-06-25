# ------------------------------- Recursive Postorder Traversal -------------------------------
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root

# ------------------------------- Iterative Postorder Traversal Using Two Stacks -------------------------------
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        s1 = [(root, None, None)]
        s2 = []

        while s1:
            node, parent, is_left = s1.pop()
            if node:
                s2.append((node, parent, is_left))
                s1.append((node.left, node, True))
                s1.append((node.right, node, False))

        while s2:
            node, parent, is_left = s2.pop()
            if not node.left and not node.right and node.val == target:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None

                else:
                    root = None

        return root
