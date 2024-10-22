class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
            if cbit == 1:
                if (abit | bbit) != 1:
                    flips += 1
            else:
                if abit == 1:
                    flips += 1
                if bbit == 1:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
