class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        for i, height in enumerate(heights):
            while buildings and heights[buildings[-1]] <= height:
                buildings.pop()
            buildings.append(i)
        return buildings

------------------------------------------------------------------------------------

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = [len(heights) - 1]
        max_height = heights[-1]
        for i in range(len(heights) -1, -1, -1):
            height = heights[i]
            if height > max_height:
                buildings.append(i)
                max_height = height
        return buildings[::-1]