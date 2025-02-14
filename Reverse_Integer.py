class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0
        while x:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        reversed_x *= sign
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
        return reversed_x
