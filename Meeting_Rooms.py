class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last_end = -1
        for start, end in intervals:
            if last_end <= start:
                last_end = end
            else:
                return False
        return True
