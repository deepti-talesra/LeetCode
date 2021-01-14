class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] 
        for i in range(len(nums)-1, 0, -1):
            output.append(output[-1]*nums[i])
        output = output[::-1]
        left = 1
        for i in range(len(nums)):
            output[i] = output[i]*left
            left *= nums[i]
        return output
