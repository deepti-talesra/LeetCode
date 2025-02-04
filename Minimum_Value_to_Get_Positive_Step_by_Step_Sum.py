class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningSum = 0
        minSum = 0
        for num in nums:
            runningSum += num
            minSum = min(minSum, runningSum)
        return -minSum + 1 if minSum < 1 else 1
