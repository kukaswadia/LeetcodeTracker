# -------------------------------- Breadth-First Search (BFS) with Queue --------------------------------

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        level_index = 0

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_index % 2 == 1:
                level_nodes.reverse()

            result.append(level_nodes)
            level_index += 1

        return result

# -------------------------------- Depth-First Search (DFS) Recursion --------------------------------

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def dfs(node, level):
            if not node:
                return
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i].reverse()

        return levels

# -------------------------------- Iterative Using Two Stacks --------------------------------

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        current_level = [root]
        next_level = []
        left_to_right = True
        level_nodes = []

        while current_level:
            node = current_level.pop()
            level_nodes.append(node.val)

            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

            if not current_level:
                result.append(level_nodes)
                level_nodes = []
                current_level, next_level = next_level, []
                left_to_right = not left_to_right

        return result
