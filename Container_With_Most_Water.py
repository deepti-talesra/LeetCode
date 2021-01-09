class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        max_area = 0
        while beg < end:
            max_area = max(max_area, min(height[beg], height[end])*(end-beg))
            if height[beg] >= height[end]:
                end -= 1
            else:
                beg += 1
        return max_area 
        
