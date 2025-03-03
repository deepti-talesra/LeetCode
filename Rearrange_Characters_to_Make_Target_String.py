class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)
        return min(s_counts[char]//target_counts[char] for char in target_counts)
