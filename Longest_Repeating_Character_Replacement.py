from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = right = 0
        max_len = 0
        max_count = 0
        while right < len(s):
            counts[s[right]] += 1
            max_count = max(max_count, counts[s[right]])
            while max_count + k < right - left + 1:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
