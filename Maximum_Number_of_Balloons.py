class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in count:
                count[char] += 1
        return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"])
