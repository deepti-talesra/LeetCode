class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero + 1
                zero = i
            max_len = max(max_len, i - start)
        return max_len
