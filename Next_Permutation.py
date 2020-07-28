# Video Explanation: https://www.youtube.com/watch?v=9xT2Xzlo4i4&t=1s

class Solution:
    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp
        
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums, next_num, dec)
