class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = prices[0]
        curmax = prices[0]
        profit = 0


        for price in prices:
            if curmin > price:
                curmin = price

            else:
                profit = max(profit, price - curmin)

        return profit