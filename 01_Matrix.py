class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    mat[row][col] = float('inf')

        while queue:
            r, c = queue.popleft()
            check = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
            for row, col in check:
                if 0 <= row < rows and 0 <= col < cols and mat[row][col] > mat[r][c] + 1:
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat
