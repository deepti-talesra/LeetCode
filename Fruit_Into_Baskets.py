class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        end = 0
        max_len = 0
        d = {}
        while end < len(tree):
            d[tree[end]] = end
            if len(d) >= 3:
                min_val = min(d.values())
                del d[tree[min_val]]
                start = min_val + 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
