# ------------------------------- DFS Recursive (Preorder Traversal) ---------------------------------

class Codec:

    def serialize(self, root):
        def helper(node):
            if not node:
                return "X,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)

        return helper(root)

    def deserialize(self, data):
        values = data.split(',')

        def helper():
            val = values.pop(0)

            if val == "X":
                return None

            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        return helper()

# ------------------------------- BFS Iterative (Level Order Traversal) ---------------------------------

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("X")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        index = 1

        while queue:
            current = queue.popleft()
            if nodes[index] != "X":
                current.left = TreeNode(int(nodes[index]))
                queue.append(current.left)
            index += 1

            if nodes[index] != "X":
                current.right = TreeNode(int(nodes[index]))
                queue.append(current.right)
            index += 1

        return root

