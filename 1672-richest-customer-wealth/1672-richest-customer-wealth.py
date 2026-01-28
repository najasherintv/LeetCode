class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0

        for customer in accounts :
            total = sum(customer)
            max_wealth = max(max_wealth, total)

        return max_wealth