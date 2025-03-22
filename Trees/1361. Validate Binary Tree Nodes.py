class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
            elif indegree[i] > 1:
                return False

        if root == -1:
            return False

        visited = set()

        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            if not dfs(leftChild[node]):
                return False
            if not dfs(rightChild[node]):
                return False
            return True

        if not dfs(root):
            return False
        return len(visited) == n