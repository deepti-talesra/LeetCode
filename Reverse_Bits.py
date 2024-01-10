class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            reversed_n = (reversed_n << 1) | (n & 1)
            n >>= 1
        return reversed_n
