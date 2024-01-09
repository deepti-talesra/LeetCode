class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i!= 0 and nums[i] == nums[i-1]:
                continue
            # 2 sum on the remainder of the list
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l +=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret
