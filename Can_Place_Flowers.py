class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
