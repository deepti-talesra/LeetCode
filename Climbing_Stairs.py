class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1, 2]
        for step in range(3, n+1):
            ways.append(ways[step-1]+ways[step-2])
        return ways[n]
         # Alt solution:
         # return round(( (( 1 + 5**(1/2) )/2 )**(n+1) ) / (5**(1/2)))
