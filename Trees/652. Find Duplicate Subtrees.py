class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serial_count = defaultdict(int)
        duplicates = []

        def postorder(node):
            if not node:
                return None
            left_tuple = postorder(node.left)
            right_tuple = postorder(node.right)

            serial = (node.val, left_tuple, right_tuple)
            serial_count[serial] += 1

            if serial_count[serial] == 2:
                duplicates.append(node)
            return serial

        postorder(root)
        return duplicates