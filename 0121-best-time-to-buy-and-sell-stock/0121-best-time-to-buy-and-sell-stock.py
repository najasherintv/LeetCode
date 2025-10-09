class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        profit = 0
        while right < len(prices):

            if prices[right] >prices[left]:
                current_profit = prices[right] - prices[left]
                profit = max(profit, current_profit)
            else:
                   left = right

            right += 1   
        return profit                