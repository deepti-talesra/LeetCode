class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        pop = points[0][1]
        arrow = 1
        for start, end in points:
            if start > pop:
                arrow += 1
                pop = end
        return arrow
