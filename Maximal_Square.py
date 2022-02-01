class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    max_edge = max(max_edge, int(matrix[row][col]))
                elif matrix[row][col] == '1':
                    matrix[row][col] = min(int(matrix[row-1][col]), int(matrix[row-1][col-1]), int(matrix[row][col-1])) + 1
                    max_edge = max(max_edge, matrix[row][col])
        return max_edge**2
