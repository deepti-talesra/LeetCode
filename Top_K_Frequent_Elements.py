from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        heap = []
        for key, val in d.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
