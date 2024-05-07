class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def comb(beg, curr):
            if len(curr) == k:
                result.append(curr)
                return
            if len(curr) > k:
                return
            for ind in range(beg, n + 1):
                comb(ind + 1, curr + [ind])
        comb(1, [])
        return result
