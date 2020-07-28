# Video Explanation: https://www.youtube.com/watch?v=re7fhVyKWZI

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        
        for i in nums:
            pos = abs(i) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
                
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)
                
        return missing
