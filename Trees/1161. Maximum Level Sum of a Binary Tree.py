# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from multiprocessing.synchronize import RECURSIVE_MUTEX

                                                        # // Iterative
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_num = 1
        max_sum = root.val
        level = [root]
        ret = 1

        while level != []:
            next_level = []
            level_sum = 0
            level_num += 1

            for roots in level:
                if roots.left:
                    next_level.append(roots.left)
                    level_sum += roots.left.val
                if roots.right:
                    next_level.append(roots.right)
                    level_sum += roots.right.val

            if next_level != [] and level_sum > max_sum:
                max_sum = level_sum
                ret = level_num

            level = next_level
        return ret

                                                        # // Recursive


class Solution:
    def helper(self, root, level):
        if root:
            self.level[level] += root.val
            self.helper(root.left, level + 1)
            self.helper(root.right, level + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.level = defaultdict(int)
        self.helper(root, 1)

        return sorted(self.level.items(), key=lambda x: x[1], reverse=True)[0][0]


