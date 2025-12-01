class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only using two boolean variables
        """
        increasing = True
        decreasing = True 

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums [i] < nums[i - 1]:
                increasing = False

            if not increasing and not decreasing:
                return False

        return increasing or decreasing 