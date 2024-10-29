class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums) + 1
        start = end = 0
        curr_sum = 0
        
        for end in range(len(nums)):
            curr_sum += nums[end]
            
            while curr_sum >= target:
                size = min(size, end - start + 1)
                curr_sum -= nums[start]
                start += 1
        return size if size != len(nums) + 1 else 0
