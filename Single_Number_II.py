class Solution:
    # 2 var (more concise) solution
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for num in nums:
            once ^= num & ~twice
            twice ^= num & ~once
        return once
      
    # 3 var (more readable) solution
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for num in nums:
            twice |= once & num
            once ^= num
            thrice = once & twice
            
            once &= ~thrice
            twice &= ~thrice
        return once
