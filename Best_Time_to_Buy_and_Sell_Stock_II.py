class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > buy:
                profit += price - buy
            buy = price
        return profit
