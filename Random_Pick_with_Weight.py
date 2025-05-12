class Solution:

    def __init__(self, w: List[int]):
        self.range = -1
        self.ranges = []
        for weight in w:
            self.range += weight
            self.ranges.append(self.range)

        
    def pickIndex(self) -> int:
        rand_num = random.randint(0, self.range) #105
        left, right = 0, len(self.ranges) - 1
        while left < right:
            mid = (left + right)//2
            if self.ranges[mid] < rand_num:
                left = mid + 1
            else:
                right = mid
        return left
