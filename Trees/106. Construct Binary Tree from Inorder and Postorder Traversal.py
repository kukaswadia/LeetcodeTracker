# --------------------------- Brute Force Recursive Approach (Without a Dictionary) -----------------------------

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        index = inorder.index(root_val)

        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

# --------------------------- Optimized Recursive Approach (Using a Dictionary) -----------------------------

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}
        post_index = len(postorder) - 1

        def helper(in_left, in_right):
            nonlocal post_index

            if in_left > in_right:
                return None

            root_val = postorder[post_index]
            post_index -= 1
            root = TreeNode(root_val)

            index = inorder_map[root_val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        return helper(0, len(inorder) - 1)

# --------------------------- Iterative Approach Using a Stack -----------------------------

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        post_index = len(postorder) - 1
        in_index = len(inorder) - 1

        root = TreeNode(postorder[post_index])
        stack = [root]
        post_index -= 1

        while post_index >= 0:
            current = stack[-1]

            if current.val != inorder[in_index]:
                node = TreeNode(postorder[post_index])
                current.right = node
                stack.append(node)
                post_index -= 1
            else:
                while stack and stack[-1].val == inorder[in_index]:
                    current = stack.pop()
                    in_index -= 1
                if post_index >= 0:
                    node = TreeNode(postorder[post_index])
                    current.left = node
                    stack.append(node)
                    post_index -= 1
        return root