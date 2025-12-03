class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = 0
        
        # Traverse from right to left
        for i in range(len(heights) - 1, -1, -1):
            # If current building is taller than all buildings to its right
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]
        
        # Reverse to get indices in ascending order
        result.reverse()
        return result