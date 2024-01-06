class Solution:
    # Recursive Solution
    def find(self, beg, end, nums):
        if end <= beg:
            return nums[end]
        mid = (beg + end)//2
        if nums[mid] > nums[end]:
            return self.find(mid + 1, end, nums)
        else:
            return self.find(beg, mid, nums)
    
    def findMin(self, nums: List[int]) -> int:
        return self.find(0, len(nums)-1, nums)

    # Iterative Solution
    def findMin(self, nums: List[int]) -> int:
        beg,end = 0, len(nums) - 1
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] > nums[end]:
                beg = mid + 1
            else:
                end = mid
        return nums[end]
