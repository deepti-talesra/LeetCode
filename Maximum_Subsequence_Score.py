import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums2))]
        pairs.sort(key = lambda x: x[1], reverse = True)
        
        max_score = 0
        curr_sum = 0
        heap = []
        
        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            
            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, curr_sum * n2)
        return max_score
