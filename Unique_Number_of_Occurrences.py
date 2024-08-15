from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        occur = list(counts.values())
        return len(occur) == len(set(occur))
