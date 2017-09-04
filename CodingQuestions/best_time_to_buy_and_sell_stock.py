"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_index = 0
        sell_index = 0
        for index in range(len(prices)):
            profit = prices[index] - prices[buy_index]
            if profit > max_profit:
                max_profit = profit
                sell_index = index
            elif prices[index] < prices[buy_index]:
                buy_index = index
        return max_profit