class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        output = [[0]*rows for i in range(cols)]
        for r in range(rows):
            for c in range(cols):
                output[c][r] = matrix[r][c]
        return output
