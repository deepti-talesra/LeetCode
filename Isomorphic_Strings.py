class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        values = set()
        for i, char in enumerate(s):
            if char not in d:
                if t[i] in values:
                    return False
                d[char] = t[i]
                values.add(t[i])
            else:
                if d[char] != t[i]:
                    return False
        return True
