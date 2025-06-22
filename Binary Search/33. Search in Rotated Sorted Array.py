class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums) - 1
        while beg < end:
            mid = (beg + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[beg]:
                if nums[beg] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    beg = mid + 1
            elif nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid - 1

        return -1 if nums[end] != target else beg
