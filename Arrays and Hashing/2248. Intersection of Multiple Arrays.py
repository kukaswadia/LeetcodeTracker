class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Initialize the result set with the first sub array
        result = set(nums[0])

        # Intersect with the set representation of each subsequent array
        # &= is the intersection update operator 
        for arr in nums[1:]:
            result &= set(arr)
        
        # return the sorted list of intersected elements
        return sorted(result)
