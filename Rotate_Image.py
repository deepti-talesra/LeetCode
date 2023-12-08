class Solution:
  
  # First Approach
  def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # First transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

  
    # Second Approach
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        end = n - 1

        for row in range(n//2):
            for col in range(row, end-row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[end-col][row]
                matrix[end-col][row] = matrix[end - row][end-col]
                matrix[end - row][end-col] = matrix[col][end - row]
                matrix[col][end - row] = temp
