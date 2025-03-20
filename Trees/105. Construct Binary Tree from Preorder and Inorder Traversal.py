# ----------------------------------- Optimized Recursive Approach Using a Dictionary -----------------------------------

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: idx for idx, value in enumerate(inorder)}
        pre_idx = [0]

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)
            pre_idx[0] += 1
            index = inorder_index[root_val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)

# ----------------------------------- Iterative Approach Using a Stack -----------------------------------

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for value in preorder[1:]:
            node = TreeNode(value)

            if stack[-1].val != inorder[inorder_index]:
                stack[-1].left = node
            else:
                last = None
                while stack and stack[-1].val == inorder[inorder_index]:
                    last = stack.pop()
                    inorder_index += 1
                last.right = node
            stack.append(node)
        return root