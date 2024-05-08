from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)
        for char in magazine:
            d[char] += 1
        for char in ransomNote:
            if char not in d or d[char] <= 0:
                return False
            d[char] -= 1
        return True
