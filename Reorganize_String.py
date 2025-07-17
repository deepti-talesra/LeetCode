class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        if -heap[0][0] > (len(s) + 1) // 2:
            return ""
        prev = (0, "")
        res = ""
        while heap:
            count, char = heapq.heappop(heap)
            res += char
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (count + 1, char)
        return res
