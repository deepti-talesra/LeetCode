class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = []
        minutes = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        while rotten and fresh > 0:
            minutes += 1
            curr = []
            for r,c in rotten:
                check = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for i,j in check:
                    if i>=0 and j>=0 and i<rows and j<cols and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        curr.append((i,j))
                        if fresh == 0:
                            return minutes
            rotten = curr
        if fresh == 0:
            return minutes
        else:
            return -1
