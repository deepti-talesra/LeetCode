# Video Explanation: https://www.youtube.com/watch?v=CHlCkJadQ7o

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lst = sorted(d.values(), reverse = True)
        max_number = lst[0]
        
        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_number:
            counter += 1
            i += 1
        
        ret = (max_number - 1) * (n + 1) + counter
        return max(ret, len(tasks))
