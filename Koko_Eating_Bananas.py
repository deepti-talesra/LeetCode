class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high)//2
            hours = 0
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1
            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return low
