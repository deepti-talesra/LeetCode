class Solution:
    # Brian Kernighan's algorithm
    def hammingWeight(self, n: int) -> int:
        counts = 0
        while n:
            n = n & (n-1)
            counts += 1
        return counts

    # Simple approach
    def hammingWeight(self, n: int) -> int:
      counts = 0
      while n:
          counts += n&1
          n >>= 1
      return counts
   
  
  
