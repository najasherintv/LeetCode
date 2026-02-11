class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        digit=list(map(int, str(n)))
        for i in digit:
            p*=i
        return p-sum(digit)    
        