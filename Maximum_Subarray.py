class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0 
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
      
    # Another similar solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_sum = curr
        for ind in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[ind]
            max_sum = max(max_sum, curr)
        return max_sum
