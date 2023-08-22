class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1
        while left <= right:
            middle_ind = (left + right)//2
            middle = nums[middle_ind]
            if middle > target:
                right = middle_ind - 1
            elif middle < target:
                left = middle_ind + 1
            elif middle == target:
                return middle_ind
        return -1 
