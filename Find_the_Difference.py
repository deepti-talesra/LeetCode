# Video Explanation: https://www.youtube.com/watch?v=qsrmeOn7NrE

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_sum = 0
        for i in t:
            t_sum += ord(i)
        for i in s:
            t_sum -= ord(i)
        return chr(t_sum)
