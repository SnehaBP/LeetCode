class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        else:
            profit=0
            min_prize=prices[0]
            for price in prices:
                min_prize=min(min_prize,price)
                profit=max(profit,price-min_prize)
            return profit