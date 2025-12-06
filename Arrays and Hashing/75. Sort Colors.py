class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap with low pointer and move forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                # Already in correct position -> move mid
                mid += 1
            else:
                # nums[mid] == 2
                # swap with high pointer and move high back
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1