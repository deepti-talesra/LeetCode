class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = max_p = nums[0]
        maximum_product = max_p
        for num in nums[1:]:
            temp = min_p
            min_p = min(num, num*min_p, num*max_p)
            max_p = max(num, num*temp, num*max_p)
            maximum_product = max(max_p, maximum_product)
        return maximum_product
