class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        dp = [[False for _ in range(n+1)] for _ in range(m + 1)]
        dp[0][0] = True

        for r in range(m + 1):
            for c in range(n + 1):
                if c > 0 and dp[r][c-1] and s1[c-1] == s3[c-1+r]:
                    dp[r][c] = True
                elif r > 0 and dp[r-1][c] and s2[r-1] == s3[r-1+c]:
                    dp[r][c] = True
        return dp[-1][-1]
