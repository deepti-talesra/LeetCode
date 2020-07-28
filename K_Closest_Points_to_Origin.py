# Video Explanation: https://www.youtube.com/watch?v=3OxgmzezTG8

import random
class Solution:
    
    def find(self, lst, K):
        if len(lst) == K:
            return [i[0] for i in lst]
        rand_tup = random.choice(lst)
        pivot = rand_tup[1]
        
        i = 0
        left = []
        right = []
        equal = []
        
        while i < len(lst):
            curr = lst[i]
            dist = curr[1]
            if dist < pivot:
                left.append(curr)
            elif dist == pivot:
                equal.append(curr)
            else:
                right.append(curr)
            i += 1
        len_left = len(left)
        if len_left == K:
            return [i[0] for i in left]
        if len_left + len(equal) == K:
            return [i[0] for i in left] + [i[0] for i in equal]
        if K < len_left:
            return self.find(left, K)
        else:
            return [i[0] for i in left] + [i[0] for i in equal] + self.find(right, K - len_left - len(equal)) 
    
    
    def dist(self, pt):
        return pt[0] ** 2 + pt[1] ** 2
    
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        lst = [(i, self.dist(i)) for i in points]
        return self.find(lst, K)
