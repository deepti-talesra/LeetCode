class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        p1, p2 = 0, len(nums) - 1
        ind = len(nums) - 1
        while ind >= 0:
            if abs(nums[p2]) > abs(nums[p1]):
                output[ind] = nums[p2]*nums[p2]
                p2 -= 1
            else:
                output[ind] = nums[p1]*nums[p1]
                p1 += 1
            ind -= 1
        return output
