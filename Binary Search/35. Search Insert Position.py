# ---------------------------------------------------------------------
# Iterative Solution

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# ---------------------------------------------------------------------
# Recursive Solution

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def find(left, right):
            if left > right:
                return left
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return find(mid + 1, right)
            else:
                return find(left, mid - 1)

        return find(0, len(nums) - 1)