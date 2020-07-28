# Video Explanation: https://www.youtube.com/watch?v=fA_4_LuVpZ8

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            if i > right:
                return False
            if nums[i] + i > right:
                right = nums[i] + i
            if right >= last:
                return True
