class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        merged = ""
        len_w1 = len(word1)
        len_w2 = len(word2)
        while i < len_w1 and j < len_w2:
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len_w1:
            merged += word1[i:]
        else:
            merged += word2[j:]
        return merged
