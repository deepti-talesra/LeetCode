class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = [len(heights)-1]
        max_height = heights[-1]
        for i in range(len(heights)-2, -1, -1):
            height = heights[i]
            if height > max_height:
                buildings.append(i)
                max_height = height
        return buildings[::-1]
