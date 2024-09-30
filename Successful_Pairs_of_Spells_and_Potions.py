class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for spell in spells:
            low, high = 0, len(potions)
            while low < high:
                mid = (low + high)//2
                if potions[mid] * spell >= success:
                    high = mid
                else: 
                    low = mid + 1
            pairs.append(len(potions)-low)
        return pairs
