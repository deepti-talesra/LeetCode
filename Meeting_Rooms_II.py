import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        meeting_rooms = 1
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            meeting_rooms = max(meeting_rooms, len(heap))
        return meeting_rooms
