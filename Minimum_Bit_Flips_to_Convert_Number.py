class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        xor = start ^ goal

        while xor:
            xor = xor & (xor - 1)
            flips += 1
        return flips  
