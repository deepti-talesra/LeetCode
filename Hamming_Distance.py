class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        xor = x ^ y
        while xor:
            xor = xor & (xor-1)
            dist += 1
        return dist
