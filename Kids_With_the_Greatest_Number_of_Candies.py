class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
