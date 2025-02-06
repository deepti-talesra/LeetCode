class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x*10 + x % 10
            x //= 10
        return x == reversed_x or x == reversed_x//10
