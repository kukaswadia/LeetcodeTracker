class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) 
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid
            elif target > nums[mid]:
                low = mid + 1
        return low


# -------------------------------OR ------------------------------- (Spot the Differences with positioning of high)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return low