class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind in range(len(nums)):
            num = nums[ind]
            if target - num in seen:
                return [ind, seen[target-num]]
            seen[num] = ind
