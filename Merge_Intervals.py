# Video Explanation: https://www.youtube.com/watch?v=5EY9rHCfa8g&feature=youtu.be

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        result = []
        # sort by start times
        intervals.sort()
        for interval in intervals:
            # if the last interval has ended before the current one starts: add new interval 
            if result == [] or result[-1][1] < interval[0]]:
                result.append(interval)
            # there is overlap: merge
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
