from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0]
        max_profit = float('-inf')
        for i in range(1, len(prices)):
            min_buy_price = min(min_buy_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy_price)
        if max_profit == float('-inf'):
            return 0
        return max_profit