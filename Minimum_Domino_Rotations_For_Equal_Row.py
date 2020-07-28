# Video Explanation: https://www.youtube.com/watch?v=67pTegSngpY

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_counts = [0]*7
        b_counts = [0]*7
        
        same = 0
        
        for i in range(len(A)):
            a_counts[A[i]] += 1
            b_counts[B[i]] += 1
            
            if A[i] == B[i]:
                same += 1
                
        for i in range(1, 7):
            if a_counts[i] + b_counts[i] - same == len(A):
                return len(A) - max(a_counts[i], b_counts[i])
            
        return -1
