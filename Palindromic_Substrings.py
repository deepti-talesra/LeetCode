class Solution:
    def palindrome(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    def countSubstrings(self, s: str) -> int:
        counts = 0
        for i in range(len(s)):
            counts += self.palindrome(s, i, i)
            counts += self.palindrome(s, i, i+1)
        return counts
