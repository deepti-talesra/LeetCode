class Solution:
    
    def reach(self, row, col, ocean, heights):
        ocean[row][col] = True
        check = [[row+1, col], [row-1, col], [row, col+1], [row,col-1]]
        for r, c in check:
            if 0 <= r < len(ocean) and 0 <= c < len(ocean[0]) and not ocean[r][c] and heights[r][c] >= heights[row][col]:
                self.reach(r, c, ocean, heights)
        return 
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows, cols = len(heights), len(heights[0])
        atl = [[False for i in range(cols)] for j in range(rows)]
        pac = [[False for i in range(cols)] for j in range(rows)]
        
        
        for i in range(cols):
            self.reach(0, i, pac, heights)
            self.reach(rows-1, i, atl, heights)
        for i in range(rows):
            self.reach(i, 0, pac, heights)
            self.reach(i, cols-1, atl, heights)
        
        for row in range(rows):
            for col in range(cols):
                if atl[row][col] and pac[row][col]:
                    result.append([row,col])
        return result
