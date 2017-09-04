"""
Say you have an array for which the ith element is the
price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm
to find the maximum profit.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_index = 0
        for i, price in enumerate(prices):
            profit = price - prices[buy_index]
            if profit > max_profit:
                max_profit = profit
            elif price < prices[buy_index]:
                buy_index = i
        return max_profit
