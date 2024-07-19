class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        profit=0
        for i in prices:
            if i<min_price:
                min_price=i
            pr=i-min_price

            if pr>profit:
                profit=pr
        return profit
        