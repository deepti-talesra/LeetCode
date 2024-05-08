class Solution:
    
    def calc(self, n):
        curr = 0
        while n > 0:
            digit = n % 10
            curr += digit * digit
            n //= 10
        return curr
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.calc(n)
            if n in seen:
                return False
            seen.add(n)
        return True
