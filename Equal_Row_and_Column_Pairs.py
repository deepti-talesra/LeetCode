from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            if column in rows:
                pairs += rows[column]
        return pairs
