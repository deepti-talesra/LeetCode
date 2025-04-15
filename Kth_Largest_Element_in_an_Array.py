class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r):
            less, equal, greater, pivot = l, l, r, nums[r]
            while equal <= greater:
                while equal <= greater and nums[equal] < pivot:
                    nums[equal], nums[less] = nums[less], nums[equal]
                    less += 1
                    equal += 1
                while equal <= greater and nums[equal] == pivot:
                    equal += 1
                while equal <= greater and nums[equal] > pivot:
                    nums[equal], nums[greater] = nums[greater], nums[equal]
                    greater -= 1
                
            if k > greater:
                return quickSelect(greater + 1, r)
            elif k < less:
                return quickSelect(l, less - 1)
            else:
                return nums[greater]


        return quickSelect(0, len(nums)-1)
