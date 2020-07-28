# Video Explanation: https://www.youtube.com/watch?v=gp_wfYhjALw
# Video Explanation Part 2: https://www.youtube.com/watch?v=vxN-I83so4I

class Solution:
    # VIDEO 2 Solutions - Optimized
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1)))
        
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp = []
        for i in range(m):
            dp.append(1)
        for row in range(1, n):
            for col in range(1, m):
                dp[col] += dp[col - 1]
        return dp[-1]
        
    # VIDEO 1 Solution
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2) / (factorial(m-1)*factorial(n-1)))
        if m == n == 1:
            return 1
        dp = [[1]*m]*n
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]
