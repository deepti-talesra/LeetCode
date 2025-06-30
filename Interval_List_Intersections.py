class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        ind1 = 0
        ind2 = 0
        while ind1 < len(firstList) and ind2 < len(secondList):
            start = max(firstList[ind1][0], secondList[ind2][0])
            end = min(firstList[ind1][1], secondList[ind2][1])
            if start <= end:
                output.append([start, end])
            if firstList[ind1][1] < secondList[ind2][1]:
                ind1 += 1
            else:
                ind2 += 1
        return output
