class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        while left < right:
            if left_max < right_max:
                water_trapped += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                water_trapped += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return water_trapped
