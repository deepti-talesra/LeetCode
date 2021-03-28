class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        d = {}
        while end < len(s):
            d[s[end]] = end
            if len(d) > 2:
                min_ind = min(d.values())
                start = min_ind + 1
                del d[s[min_ind]]
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
